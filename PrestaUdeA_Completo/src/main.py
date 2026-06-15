from persistencia import inicializar_archivos, cargar_json, guardar_json
from validaciones import (
    validar_nombre_persona,
    validar_nombre_item,
    validar_documento,
    validar_correo,
    validar_tiempo_prestamo,
    validar_categoria,
    validar_precio,
    validar_estado_item,
    CATEGORIAS_VALIDAS,
    ESTADOS_DIFUSOS,
)
from clsUsuarios import clsUsuarios
from clsPrestamo import clsPrestamo
from item import Item
from utilidades import (
    generar_id_item,
    generar_id_prestamo,
    fecha_hoy,
    sumar_dias,
    fecha_a_texto,
    texto_a_fecha,
    dias_transcurridos,
)
from reportes import generar_reporte_prestamos_ordenados
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CERTIFICADOS_DIR = BASE_DIR / "certificados"
FACTURAS_DIR = BASE_DIR / "facturas"


def registrar_auditoria(usuario, accion):
    auditoria = cargar_json("auditoria")
    auditoria.append({"usuario": usuario, "accion": accion, "fecha": fecha_a_texto(fecha_hoy())})
    guardar_json("auditoria", auditoria)


def buscar_usuario_por_documento(documento):
    usuarios = cargar_json("usuarios")
    for usuario in usuarios:
        if usuario["documento"] == documento and usuario.get("activo", True):
            return usuario
    return None


def buscar_item_por_id(item_id):
    items = cargar_json("items")
    for item in items:
        if item["item_id"] == item_id:
            return item
    return None


def registrar_usuario():
    print("\n=== REGISTRO DE USUARIO ===")
    nombre = input("Nombre: ").strip()
    if not validar_nombre_persona(nombre):
        print("Nombre inválido.")
        return

    apellido = input("Apellido: ").strip()
    if not validar_nombre_persona(apellido):
        print("Apellido inválido.")
        return

    documento = input("Documento: ").strip()
    if not validar_documento(documento):
        print("Documento inválido.")
        return

    if buscar_usuario_por_documento(documento):
        print("Ya existe un usuario con ese documento.")
        return

    correo = input("Correo electrónico: ").strip()
    if not validar_correo(correo):
        print("Correo inválido.")
        return

    try:
        tiempo_prestamo = int(input("Tiempo de préstamo (5, 10, 15 o 30): ").strip())
    except ValueError:
        print("Tiempo inválido.")
        return

    if not validar_tiempo_prestamo(tiempo_prestamo):
        print("Tiempo no permitido.")
        return

    usuarios = cargar_json("usuarios")
    usuario = clsUsuarios(nombre, apellido, documento, correo, tiempo_prestamo)
    usuarios.append(usuario.to_dict())
    guardar_json("usuarios", usuarios)
    registrar_auditoria(documento, "Registro de usuario")
    print("Usuario registrado correctamente.")


def listar_usuarios():
    usuarios = cargar_json("usuarios")
    print("\n=== LISTA DE USUARIOS ===")
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in usuarios:
        print(f"{usuario['nombre']} {usuario['apellido']} - Documento: {usuario['documento']} - Tiempo: {usuario['tiempo_prestamo']} días")


def registrar_item():
    print("\n=== REGISTRO DE ÍTEM ===")
    nombre = input("Nombre del ítem: ").strip()
    if not validar_nombre_item(nombre):
        print("Nombre inválido.")
        return

    print("Categorías válidas:")
    for categoria in CATEGORIAS_VALIDAS:
        print(f"- {categoria}")
    categoria = input("Categoría: ").strip()
    if not validar_categoria(categoria):
        print("Categoría inválida.")
        return

    try:
        precio = float(input("Precio de compra: ").strip())
    except ValueError:
        print("Precio inválido.")
        return

    if not validar_precio(precio):
        print("El precio no puede ser negativo.")
        return

    print("Estados válidos:")
    for estado in ESTADOS_DIFUSOS:
        print(f"- {estado}")
    estado = input("Estado del ítem: ").strip().title()
    if not validar_estado_item(estado):
        print("Estado inválido.")
        return

    items = cargar_json("items")
    item_id = generar_id_item(categoria, len(items) + 1)
    item = Item(item_id, nombre, categoria, precio, estado)
    items.append(item.to_dict())
    guardar_json("items", items)
    registrar_auditoria("admin", f"Registro de ítem {item_id}")
    print(f"Ítem registrado correctamente con ID: {item_id}")


def listar_items(disponibles_solo=False):
    items = cargar_json("items")
    print("\n=== LISTA DE ÍTEMS ===")
    filtrados = [item for item in items if item["disponible"]] if disponibles_solo else items
    if not filtrados:
        print("No hay ítems para mostrar.")
        return []
    for item in filtrados:
        disponibilidad = "Disponible" if item["disponible"] else "Prestado"
        print(f"{item['item_id']} - {item['nombre']} - {item['categoria']} - ${item['precio_compra']:.2f} - {item['estado']} - {disponibilidad}")
    return filtrados


def registrar_prestamo():
    print("\n=== REGISTRO DE PRÉSTAMO ===")
    documento = input("Documento del usuario: ").strip()
    usuario = buscar_usuario_por_documento(documento)
    if not usuario:
        print("El usuario no existe. Debe registrarlo primero.")
        return

    disponibles = listar_items(disponibles_solo=True)
    if not disponibles:
        return

    item_id = input("Ingrese el ID del ítem a prestar: ").strip().upper()
    item = buscar_item_por_id(item_id)
    if not item or not item["disponible"]:
        print("Ítem no disponible o inexistente.")
        return

    prestamos = cargar_json("prestamos")
    prestamo_id = generar_id_prestamo(len(prestamos) + 1)
    salida = fecha_hoy()
    devolucion = sumar_dias(salida, usuario["tiempo_prestamo"])
    prestamo = clsPrestamo(prestamo_id, documento, item_id, fecha_a_texto(salida), fecha_a_texto(devolucion))
    prestamos.append(prestamo.to_dict())
    guardar_json("prestamos", prestamos)

    items = cargar_json("items")
    for registro in items:
        if registro["item_id"] == item_id:
            registro["disponible"] = False
            break
    guardar_json("items", items)
    registrar_auditoria(documento, f"Préstamo {prestamo_id}")
    print(f"Préstamo registrado. Fecha pactada de devolución: {fecha_a_texto(devolucion)}")


def generar_certificado(prestamo, usuario):
    CERTIFICADOS_DIR.mkdir(parents=True, exist_ok=True)
    nombre_archivo = f"{usuario['nombre']}_{prestamo['prestamo_id']}_{fecha_a_texto(fecha_hoy())}.txt".replace(" ", "_")
    ruta = CERTIFICADOS_DIR / nombre_archivo
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("CERTIFICADO DE DEVOLUCIÓN\n")
        archivo.write("=" * 40 + "\n")
        archivo.write(f"Usuario: {usuario['nombre']} {usuario['apellido']}\n")
        archivo.write(f"Documento: {usuario['documento']}\n")
        archivo.write(f"Préstamo: {prestamo['prestamo_id']}\n")
        archivo.write(f"Ítem: {prestamo['item_id']}\n")
        archivo.write(f"Fecha devolución: {fecha_a_texto(fecha_hoy())}\n")
    return ruta


def registrar_devolucion():
    print("\n=== REGISTRO DE DEVOLUCIÓN ===")
    documento = input("Documento del usuario: ").strip()
    usuario = buscar_usuario_por_documento(documento)
    if not usuario:
        print("Usuario no registrado.")
        return

    prestamos = cargar_json("prestamos")
    activos = [p for p in prestamos if p["documento_usuario"] == documento and p["estado"] == "activo"]
    if not activos:
        print("El usuario no tiene préstamos activos.")
        return

    for prestamo in activos:
        print(f"- {prestamo['prestamo_id']} | Ítem: {prestamo['item_id']} | Salida: {prestamo['fecha_salida']} | Devolución pactada: {prestamo['fecha_devolucion_pactada']}")

    prestamo_id = input("Ingrese el ID del préstamo a devolver: ").strip().upper()
    seleccionado = None
    for prestamo in prestamos:
        if prestamo["prestamo_id"] == prestamo_id and prestamo["estado"] == "activo":
            seleccionado = prestamo
            break

    if not seleccionado:
        print("Préstamo activo no encontrado.")
        return

    seleccionado["estado"] = "devuelto"
    guardar_json("prestamos", prestamos)

    devoluciones = cargar_json("devoluciones")
    devoluciones.append({
        "prestamo_id": seleccionado["prestamo_id"],
        "documento_usuario": documento,
        "item_id": seleccionado["item_id"],
        "fecha_devolucion": fecha_a_texto(fecha_hoy()),
    })
    guardar_json("devoluciones", devoluciones)

    items = cargar_json("items")
    for item in items:
        if item["item_id"] == seleccionado["item_id"]:
            item["disponible"] = True
            break
    guardar_json("items", items)

    ruta = generar_certificado(seleccionado, usuario)
    registrar_auditoria(documento, f"Devolución {prestamo_id}")
    print(f"Devolución registrada. Certificado generado en: {ruta}")


def generar_factura_venta(prestamo, usuario, item):
    FACTURAS_DIR.mkdir(parents=True, exist_ok=True)
    impuesto = item["precio_compra"] * 0.23
    subtotal = item["precio_compra"]
    total = subtotal + impuesto
    nombre_archivo = f"factura_{usuario['documento']}_{prestamo['prestamo_id']}.txt"
    ruta = FACTURAS_DIR / nombre_archivo
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("FACTURA DE VENTA\n")
        archivo.write("=" * 40 + "\n")
        archivo.write(f"Usuario: {usuario['nombre']} {usuario['apellido']}\n")
        archivo.write(f"Documento: {usuario['documento']}\n")
        archivo.write(f"Préstamo: {prestamo['prestamo_id']}\n")
        archivo.write(f"Ítem: {item['item_id']} - {item['nombre']}\n")
        archivo.write("Motivación: préstamo superior a 30 días.\n")
        archivo.write("Impuesto por conchudez: 23%\n")
        archivo.write(f"Subtotal: ${subtotal:.2f}\n")
        archivo.write(f"Impuesto: ${impuesto:.2f}\n")
        archivo.write(f"Total: ${total:.2f}\n")
    return ruta, subtotal, impuesto, total


def generar_ventas_vencidas():
    print("\n=== GENERAR VENTAS POR MORA > 30 DÍAS ===")
    prestamos = cargar_json("prestamos")
    ventas = cargar_json("ventas")
    items = cargar_json("items")
    procesadas = 0

    for prestamo in prestamos:
        if prestamo["estado"] != "activo":
            continue
        dias = dias_transcurridos(texto_a_fecha(prestamo["fecha_salida"]))
        if dias <= 30:
            continue
        if any(v["prestamo_id"] == prestamo["prestamo_id"] for v in ventas):
            continue

        usuario = buscar_usuario_por_documento(prestamo["documento_usuario"])
        item = buscar_item_por_id(prestamo["item_id"])
        if not usuario or not item:
            continue

        ruta, subtotal, impuesto, total = generar_factura_venta(prestamo, usuario, item)
        ventas.append({
            "prestamo_id": prestamo["prestamo_id"],
            "documento_usuario": usuario["documento"],
            "item_id": item["item_id"],
            "subtotal": subtotal,
            "impuesto": impuesto,
            "total": total,
            "fecha": fecha_a_texto(fecha_hoy()),
            "ruta_factura": str(ruta),
        })
        prestamo["estado"] = "vendido"
        procesadas += 1

    guardar_json("prestamos", prestamos)
    guardar_json("ventas", ventas)
    if procesadas == 0:
        print("No hay préstamos vencidos con más de 30 días para convertir en venta.")
    else:
        print(f"Ventas generadas: {procesadas}")


def login_admin():
    print("\n=== ACCESO ADMINISTRADOR ===")
    usuario = input("Usuario: ").strip()
    contrasena = input("Contraseña: ").strip()
    admins = cargar_json("admins")
    for admin in admins:
        if admin["usuario"] == usuario and admin["contrasena"] == contrasena:
            print("Acceso concedido.")
            return True
    print("Credenciales inválidas.")
    return False


def reportes_admin():
    if not login_admin():
        return

    usuarios = cargar_json("usuarios")
    prestamos = cargar_json("prestamos")
    devoluciones = cargar_json("devoluciones")
    ventas = cargar_json("ventas")

    conteo = {}
    for prestamo in prestamos:
        doc = prestamo["documento_usuario"]
        conteo[doc] = conteo.get(doc, 0) + 1

    mayor = max(conteo, key=conteo.get) if conteo else None
    menor = min(conteo, key=conteo.get) if conteo else None
    total_pago = sum(v["total"] for v in ventas)

    print("\n=== REPORTES ADMINISTRATIVOS ===")
    print(f"Total de préstamos registrados: {len(prestamos)}")
    print(f"Total de ítems devueltos: {len(devoluciones)}")
    print(f"Total de ventas realizadas: {len(ventas)}")
    print(f"Total pago realizado: ${total_pago:.2f}")
    print("Lista de usuarios:")
    for usuario in usuarios:
        print(f"- {usuario['nombre']} {usuario['apellido']} ({usuario['documento']})")
    print(f"Usuario con mayor cantidad de préstamos: {mayor if mayor else 'N/A'}")
    print(f"Usuario con menor cantidad de préstamos: {menor if menor else 'N/A'}")


def exportar_reportes():
    ruta = generar_reporte_prestamos_ordenados()
    print(f"Reporte generado en: {ruta}")


def menu_principal():
    while True:
        print("\n" + "=" * 55)
        print(" PRESTAUDEA - SISTEMA DE GESTIÓN DE INVENTARIO Y PRÉSTAMOS ")
        print("=" * 55)
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Registrar ítem")
        print("4. Listar ítems")
        print("5. Registrar préstamo")
        print("6. Registrar devolución")
        print("7. Generar ventas por mora")
        print("8. Reportes administrativos")
        print("9. Exportar reporte CSV")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            registrar_item()
        elif opcion == "4":
            listar_items()
        elif opcion == "5":
            registrar_prestamo()
        elif opcion == "6":
            registrar_devolucion()
        elif opcion == "7":
            generar_ventas_vencidas()
        elif opcion == "8":
            reportes_admin()
        elif opcion == "9":
            exportar_reportes()
        elif opcion == "0":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    inicializar_archivos()
    menu_principal()
