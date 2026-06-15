# PrestaUdeA
### Sistema Inteligente de Gestión de Inventario y Préstamos

> Proyecto académico desarrollado en **Python** para la gestión de inventario, préstamos, devoluciones, ventas y reportes en un entorno institucional, mediante una aplicación de consola estructurada, modular y orientada a buenas prácticas de programación. 

---

## Descripción general

**PrestaUdeA** es un sistema de consola creado como respuesta a una necesidad de organización, trazabilidad y control sobre el préstamo de artículos. El proyecto permite registrar usuarios, administrar ítems, gestionar préstamos y devoluciones, registrar ventas y mantener la información persistente mediante archivos estructurados. 

La solución fue desarrollada con enfoque modular, separando claramente la lógica del sistema, la persistencia de datos y la documentación técnica. Esto facilita tanto el mantenimiento del código como su comprensión en un contexto académico. 

---

## Objetivo

Desarrollar un programa en **Python** con interfaz de consola visualmente amigable que permita gestionar préstamos de artículos, almacenar la información mediante archivos y estructurar el proyecto de forma organizada para su implementación, documentación y control de versiones en GitHub. 

---

## Funcionalidades principales

- Registro de usuarios del sistema.
- Gestión de inventario de artículos.
- Registro y control de préstamos.
- Procesamiento de devoluciones.
- Registro de ventas asociadas a la lógica del sistema.
- Generación de reportes administrativos.
- Persistencia de datos en archivos JSON.
- Organización modular para facilitar mantenimiento y escalabilidad. 

---

## Tecnologías utilizadas

| Herramienta | Uso |
|------------|-----|
| **Python** | Implementación de la lógica del sistema |
| **JSON** | Persistencia de información del proyecto |
| **Git** | Control de versiones |
| **GitHub** | Gestión y publicación del repositorio  |
| **Markdown** | Documentación del proyecto |

---

## Estructura del repositorio

```text
PrestaUdeA_Completo/
├── README.md
├── LICENSE
├── .gitignore
├── data/
│   ├── admins.json
│   ├── auditoria.json
│   ├── devoluciones.json
│   ├── items.json
│   ├── prestamos.json
│   ├── usuarios.json
│   └── ventas.json
├── doc/
│   └── manual_usuario.md
└── src/
    ├── clsPrestamo.py
    ├── clsUsuarios.py
    ├── item.py
    ├── main.py
    ├── persistencia.py
    ├── reportes.py
    ├── utilidades.py
    └── validaciones.py
