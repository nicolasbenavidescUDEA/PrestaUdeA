# PrestaUdeA - Proyecto completo base

Proyecto de consola en Python organizado para Visual Studio Code o Visual Studio, basado en los lineamientos del trabajo final de Algoritmia y Programación.

## Estructura

- `src/main.py`: punto de entrada y menú principal.
- `src/clsUsuarios.py`: clase de usuarios.
- `src/clsPrestamo.py`: clase de préstamos.
- `src/item.py`: clase de ítems.
- `src/validaciones.py`: reglas de validación.
- `src/persistencia.py`: manejo de archivos JSON.
- `src/utilidades.py`: fechas e identificadores.
- `src/reportes.py`: exportación de reportes CSV.
- `data/`: almacenamiento persistente.
- `certificados/`: certificados de devolución en texto.
- `facturas/`: facturas de venta en texto.
- `reportes_csv/`: reportes exportados.
- `doc/manual_usuario.md`: guía básica de uso.

## Ejecución

1. Abre la carpeta en Visual Studio Code.
2. Abre una terminal dentro de `src`.
3. Ejecuta `python main.py`.
4. Usuario administrador por defecto: `admin`
5. Contraseña por defecto: `1234`

## Observaciones

Esta es una base completa y funcional para desarrollo académico. La lógica difusa del estado del ítem se implementa de forma cualitativa simple con estados: Malo, Regular, Bueno y Excelente.
