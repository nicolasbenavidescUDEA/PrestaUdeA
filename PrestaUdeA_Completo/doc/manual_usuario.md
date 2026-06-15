# Manual de usuario
## PrestaUdeA

Sistema de gestión de inventario, préstamos, devoluciones, ventas y reportes, desarrollado en Python con interfaz de consola para uso académico.

---

## Contenido

- [1. Presentación](#1-presentación)
- [2. Propósito](#2-propósito)
- [3. Requisitos](#3-requisitos)
- [4. Estructura del proyecto](#4-estructura-del-proyecto)
- [5. Inicio del sistema](#5-inicio-del-sistema)
- [6. Menú principal](#6-menú-principal)
- [7. Registro de usuarios](#7-registro-de-usuarios)
- [8. Registro de ítems](#8-registro-de-ítems)
- [9. Registro de préstamos](#9-registro-de-préstamos)
- [10. Devoluciones](#10-devoluciones)
- [11. Ventas](#11-ventas)
- [12. Consulta de préstamos](#12-consulta-de-préstamos)
- [13. Módulo administrador](#13-módulo-administrador)
- [14. Persistencia de datos](#14-persistencia-de-datos)
- [15. Recomendaciones](#15-recomendaciones)
- [16. Errores frecuentes](#16-errores-frecuentes)
- [17. Cierre](#17-cierre)

---

## 1. Presentación

**PrestaUdeA** es una aplicación de consola desarrollada en Python para administrar artículos, usuarios, préstamos, devoluciones y ventas. El sistema fue diseñado con una estructura modular que separa el código fuente, los datos y la documentación para facilitar su uso y mantenimiento.

Este manual explica de forma práctica cómo ejecutar el programa, cómo usar sus módulos principales y qué tener en cuenta durante la operación del sistema.

---

## 2. Propósito

El propósito del sistema es permitir la gestión ordenada de préstamos de artículos, registrando la información necesaria en archivos y facilitando la consulta, seguimiento y administración de las operaciones realizadas.

---

## 3. Requisitos

Para ejecutar correctamente el sistema se recomienda contar con lo siguiente:

- Python 3.10 o superior.
- Sistema operativo Windows, Linux o macOS.
- Editor como Visual Studio Code o Visual Studio.
- Carpeta del proyecto con la estructura completa.

---

## 4. Estructura del proyecto

El proyecto se encuentra organizado en carpetas para separar responsabilidades y mejorar la claridad del repositorio.

```text
PrestaUdeA_Completo/
├── data/
├── doc/
└── src/
```

Descripción general:

- **src/**: contiene el código fuente del programa.
- **doc/**: contiene la documentación del proyecto.
- **data/**: contiene los archivos JSON usados para persistencia de datos.

---

## 5. Inicio del sistema

Para iniciar el programa, se debe abrir una terminal en la carpeta raíz del proyecto y ejecutar:

```bash
python src/main.py
```

Después de la ejecución, el sistema mostrará el menú principal en consola.

---

## 6. Menú principal

Desde el menú principal el usuario puede acceder a las funciones principales del sistema.

Opciones generales del sistema:

- Registrar usuario.
- Registrar ítem.
- Registrar préstamo.
- Registrar devolución.
- Generar venta.
- Consultar estado general de préstamos.
- Ingresar al módulo administrador.
- Salir.

---

## 7. Registro de usuarios

Esta opción permite registrar nuevos usuarios dentro del sistema.

### Datos solicitados

- Nombre
- Apellido
- Documento
- Correo electrónico
- Tiempo de préstamo permitido

### Validaciones

- El nombre debe tener al menos tres letras y no puede contener números.
- El apellido debe tener al menos tres letras y no puede contener números.
- El documento debe tener entre 3 y 15 dígitos y solo puede contener números.
- El correo electrónico debe incluir `@` y terminar en `.com`.
- El tiempo de préstamo solo puede ser 5, 10, 15 o 30 días.

Si alguno de estos criterios no se cumple, el sistema solicitará corregir la información ingresada.

---

## 8. Registro de ítems

Esta opción permite registrar los objetos disponibles para préstamo en el inventario.

### Datos solicitados

- Nombre del ítem
- Categoría
- Precio de compra
- ID único
- Estado del ítem

### Categorías permitidas

- Videojuegos
- Libros
- Música y video
- Herramientas
- Dinero
- Misceláneo y varios

### Reglas básicas

- El nombre del ítem debe tener al menos tres caracteres.
- Cada ítem debe tener un identificador único.
- El estado del ítem debe registrarse como parte del control del inventario.

---

## 9. Registro de préstamos

El sistema permite crear préstamos únicamente a usuarios que ya estén registrados.

### Condiciones

- El usuario debe existir en la base de datos del sistema.
- El ítem debe existir en el inventario.
- Deben registrarse correctamente los datos del préstamo, incluyendo fechas y código del artículo.

Si el usuario no existe, el sistema mostrará un mensaje indicando que primero debe registrarse para poder realizar el préstamo.

---

## 10. Devoluciones

Esta opción permite registrar la devolución de un préstamo activo.

### Reglas de funcionamiento

- Solo se pueden registrar devoluciones de préstamos activos.
- Si el usuario no tiene préstamos activos, el sistema lo informará y no permitirá continuar.
- Si la devolución se realiza correctamente, el sistema genera un certificado en texto plano.

### Certificado

El certificado de devolución debe incluir la información relacionada con el préstamo y generarse con un nombre asociado al prestador, la fecha y el ID correspondiente.

---

## 11. Ventas

El sistema permite generar ventas cuando el tiempo de préstamo de un artículo supera los 30 días.

### Reglas de venta

- Todo préstamo superior a 30 días debe convertirse en venta.
- La factura debe incluir la motivación de la venta y sus criterios.
- Debe aplicarse un impuesto por conchudez del 23 %.
- Deben calcularse subtotal y total de los artículos involucrados.

### Comprobante

La factura se genera en un archivo de texto plano con el nombre e identificador correspondientes.

---

## 12. Consulta de préstamos

El sistema permite consultar el estado general de los préstamos, organizados según la cantidad de días transcurridos.

Esta consulta sirve para realizar seguimiento a los artículos prestados y apoyar la gestión general del inventario.

---

## 13. Módulo administrador

El sistema cuenta con un módulo de administración protegido por usuario y contraseña.

### Ingreso

Para acceder al módulo administrador, se deben ingresar credenciales válidas registradas en el sistema.

### Reportes disponibles

- Total de préstamos registrados.
- Total de ítems devueltos.
- Total de ventas realizadas.
- Total de pago realizado.
- Lista de usuarios.
- Usuario con mayor cantidad de préstamos.
- Usuario con menor cantidad de préstamos.

---

## 14. Persistencia de datos

La información del sistema se almacena en archivos JSON ubicados en la carpeta `data/`.

Archivos principales:

- `usuarios.json`
- `items.json`
- `prestamos.json`
- `devoluciones.json`
- `ventas.json`
- `admins.json`
- `auditoria.json`

Gracias a esta estructura, la información permanece disponible entre distintas ejecuciones del programa.

---

## 15. Recomendaciones

Para usar correctamente el sistema se recomienda:

- Ejecutar el programa desde la raíz del proyecto.
- Registrar usuarios antes de crear préstamos.
- Registrar adecuadamente los ítems antes de prestarlos.
- Revisar los datos antes de confirmarlos.
- No modificar manualmente los archivos JSON sin conocer su estructura.
- Usar el módulo administrador solo con credenciales autorizadas.

---

## 16. Errores frecuentes

### No se puede registrar un usuario
Verificar que el nombre y apellido no contengan números, que el documento tenga el formato correcto y que el correo cumpla las validaciones requeridas.

### No se puede registrar un préstamo
Confirmar que el usuario exista y que el ítem esté correctamente registrado.

### No se puede registrar una devolución
Verificar que el usuario tenga un préstamo activo asociado.

### No se puede ingresar al administrador
Comprobar que el usuario y la contraseña sean correctos y existan en el sistema.

---

## 17. Cierre

Para finalizar la ejecución del sistema, el usuario debe seleccionar la opción de salida en el menú principal. Esto permite cerrar el programa de manera ordenada.
