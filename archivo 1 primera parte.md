## 2. Vínculos académicos y descripción

### Programa Académico:s
* **Pregrado:** Ingeniería Industrial
* **Institución:** Universidad de Antioquia (UdeA)

### Perfiles de los Integrantes:

* **Integrante 1: [Laura Parra]**
  * **Descripción:** Estudiante orientado al análisis de datos y optimización de procesos operativos.
  * **Habilidades y Fortalezas:** Alta capacidad para el diseño lógico de algoritmos, estructuración de bases de datos relacionales y manejo técnico de la sintaxis en Python.
  * **Debilidades (Áreas de mejora):** Tendencia a sobrecomplicar el código en las etapas iniciales y dificultad para delegar tareas técnicas complejas.

* **Integrante 2: [Mariana Lopez]**
  * **Descripción:** Estudiante con enfoque en la gestión de proyectos y la ingeniería de requerimientos.
  * **Habilidades y Fortalezas:** Excelente comunicación asertiva, documentación técnica detallada en Markdown y dominio en el control de versiones y metodologías ágiles usando GitHub.
  * **Debilidades (Áreas de mejora):** Menor velocidad en la resolución de bugs complejos en entornos de desarrollo y timidez al proponer soluciones algorítmicas disruptivas.

* **Integrante 3: [Nicolas ]**
  * **Descripción:** Estudiante interesado en la investigación de operaciones y modelado de sistemas logísticos.
  * **Habilidades y Fortalezas:** Fuerte pensamiento analítico, destreza en la validación matemática de restricciones y lógica difusa aplicada al control de inventarios.
  * **Debilidades (Áreas de mejora):** Dificultad para gestionar el tiempo bajo alta presión y propensión a enfocarse excesivamente en los detalles estéticos de la interfaz de consola.

---

## 3. Nombre del proyecto y detalles

### **Nombre del Proyecto:** PrestaUdeA - Sistema Inteligente de Gestión de Inventario y Préstamos

### **Descripción del Proyecto:**
PrestaUdeA es una solución de software basada en consola desarrollada en Python, diseñada específicamente para mitigar los problemas de pérdida de control y memoria en el inventario de herramientas, consumibles y artículos varios de la oficina 21-407. El sistema permite automatizar de forma integral el registro de usuarios, el control estricto de préstamos mediante plazos personalizados, y el seguimiento cualitativo del estado de los objetos a través de lógica difusa. Además, cuenta con un módulo administrativo capaz de procesar devoluciones, aplicar recargos por retraso e insolvencia, y exportar reportes estadísticos estructurados en archivos planos y formato CSV.

### **Foto Representativa del Proyecto:**
 `./images/logo_proyecto.png` ç

![Logo PrestaUdeA](./images/logo_proyecto.png)

  ____                  _         _    _     _        _   _ 
 |  _ \  _ __  ___  ___| |_  __ _| |  | |   | |  ___ / \ | |
 | |_) || '__|/ _ \/ __| __|/ _` | |  | |   | | / __// _ \| |
 |  __/ | |  |  __/\__ \ |_| (_| | |  | |___| ||  __// ___ \_|
 |_|    |_|   \___||___/\__|\__,_|_|  |_____|_| \___/_/   \_\_
                                                            
                 [ GESTOR DE INVENTARIO Y PRÉSTAMOS ]
                    FACULTAD DE INGENIERÍA - UdeA
  ## 4. Licencia del software

El proyecto **PrestaUdeA - Sistema Inteligente de Gestión de Inventario y Préstamos** se distribuye bajo la licencia **Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)**.

Esto implica que:

- Cualquier persona puede usar, estudiar y modificar el código con fines académicos o personales.
- Es obligatorio otorgar el debido crédito al equipo desarrollador original.
- No se permite el uso del software con fines comerciales sin una autorización previa y expresa por parte de los autores.
- Las obras derivadas deben compartirse bajo la misma licencia (CC BY-NC-SA 4.0), preservando el carácter abierto y colaborativo del proyecto.
## 5. Reporte de visión

### 5.1 Descripción general del software

**PrestaUdeA** es una solución de software basada en consola, desarrollada en Python, orientada a la gestión integral del inventario y los préstamos de herramientas, consumibles y artículos varios de la oficina 21-407 de la Facultad de Ingeniería - UdeA.

El sistema busca mitigar los problemas de pérdida de control, dependencia de la memoria humana y ausencia de trazabilidad en los registros de préstamos y devoluciones. Para ello, integra módulos de registro de usuarios, administración de inventario, control de préstamos con plazos personalizados y seguimiento del estado de los objetos mediante criterios cualitativos apoyados en lógica difusa.

### 5.2 Objetivos del sistema

Los objetivos principales de PrestaUdeA son:

1. **Estandarizar y digitalizar el proceso de préstamo y devolución** de elementos en la oficina 21-407, reduciendo la informalidad y los errores manuales en los registros.
2. **Garantizar la trazabilidad de cada objeto**, asociando quién lo solicitó, en qué fecha, bajo qué plazo y en qué estado fue devuelto.
3. **Proporcionar herramientas de apoyo a la toma de decisiones**, mediante reportes estadísticos exportables en archivos planos y formato CSV, que permitan identificar niveles de uso, rotación y estado de deterioro de los elementos.
4. **Disminuir la dependencia de la memoria individual** de los encargados de la oficina, documentando de manera sistemática los movimientos de inventario.
5. **Servir como plataforma base para futuros desarrollos académicos**, facilitando que otros estudiantes puedan extender la funcionalidad del sistema (por ejemplo, conectándolo a interfaces gráficas o bases de datos externas).

### 5.3 Beneficios esperados

La implementación de PrestaUdeA genera beneficios para distintos actores:

- **Para la oficina 21-407**  
  - Mayor control sobre la disponibilidad y localización de herramientas y consumibles.  
  - Reducción de pérdidas, extravíos y conflictos asociados a la falta de evidencia sobre los préstamos.

- **Para el personal encargado del inventario**  
  - Disminución de la carga operativa relacionada con el seguimiento manual de préstamos.  
  - Acceso rápido a información histórica y reportes que facilitan la planeación de compras y reposiciones.

- **Para los usuarios (estudiantes, docentes y personal de apoyo)**  
  - Procedimiento de préstamo más claro, transparente y consistente.  
  - Mayor probabilidad de encontrar los elementos en buen estado y disponibles cuando se necesitan.

- **Para la Facultad de Ingeniería y la UdeA**  
  - Ejemplo de solución desarrollada en contexto real de la Universidad, que puede ser replicada o adaptada a otros laboratorios y oficinas.  
  - Fomento de buenas prácticas en gestión de inventarios y uso responsable de los recursos institucionales.

En conjunto, PrestaUdeA se proyecta como una herramienta robusta y extensible que, aunque nace como proyecto académico, tiene el potencial de escalar a otros entornos de la Universidad donde existan procesos de préstamo de activos físicos.
6. Especificación de requisitos

6.1 Requisitos Funcionales (RF)

Código| Requisito Funcional
RF-01| El sistema debe permitir registrar usuarios autorizados para realizar préstamos.
RF-02| El sistema debe permitir consultar información de usuarios registrados.
RF-03| El sistema debe permitir actualizar datos de usuarios.
RF-04| El sistema debe permitir registrar nuevos elementos en el inventario.
RF-05| El sistema debe permitir modificar información de los elementos.
RF-06| El sistema debe permitir consultar disponibilidad de elementos.
RF-07| El sistema debe permitir registrar préstamos asociando usuario, elemento y fecha de devolución.
RF-08| El sistema debe permitir establecer plazos personalizados para cada préstamo.
RF-09| El sistema debe impedir préstamos de elementos no disponibles.
RF-10| El sistema debe registrar devoluciones de elementos prestados.
RF-11| El sistema debe registrar el estado físico del elemento devuelto.
RF-12| El sistema debe clasificar el estado del elemento utilizando lógica difusa.
RF-13| El sistema debe identificar préstamos vencidos.
RF-14| El sistema debe calcular recargos por retraso.
RF-15| El sistema debe generar reportes estadísticos de uso y rotación.
RF-16| El sistema debe exportar reportes en formato TXT y CSV.
RF-17| El sistema debe conservar un historial completo de movimientos.
RF-18| El sistema debe permitir consultas históricas por usuario, fecha o elemento.
RF-19| El sistema debe permitir administración general por usuarios autorizados.
RF-20| El sistema debe almacenar información de manera persistente.

6.2 Requisitos No Funcionales (RNF)

Rendimiento

Código| Requisito
RNF-R-01| Tiempo de respuesta inferior a 2 segundos para consultas estándar.
RNF-R-02| Generación de reportes en menos de 10 segundos.
RNF-R-03| Operación continua sin degradación significativa.

Seguridad

Código| Requisito
RNF-S-01| Restricción de acceso administrativo mediante autenticación.
RNF-S-02| Protección de integridad de datos almacenados.
RNF-S-03| Control de acceso a reportes generados.
RNF-S-04| Registro de auditoría de préstamos y devoluciones.

Usabilidad

Código| Requisito
RNF-U-01| Menús claros e intuitivos.
RNF-U-02| Mensajes descriptivos para errores.
RNF-U-03| Flujo simplificado para préstamos y devoluciones.
RNF-U-04| Consistencia en la navegación.

Fiabilidad

Código| Requisito
RNF-F-01| Disponibilidad mínima del 95%.
RNF-F-02| Conservación de datos entre sesiones.
RNF-F-03| Recuperación correcta de información almacenada.
RNF-F-04| Validación de datos ingresados.

Compatibilidad

Código| Requisito
RNF-C-01| Compatibilidad con Windows, Linux y macOS.
RNF-C-02| Compatibilidad de archivos CSV con Excel, LibreOffice y Google Sheets.
RNF-C-03| Compatibilidad con Python 3.10 o superior.

---

7. Plan de Proyecto

7.1 Actividades del Proyecto

Fase 1. Levantamiento y análisis de requisitos

- Identificación de necesidades.
- Definición de alcance.
- Elaboración de requisitos.
- Validación con interesados.

Fase 2. Diseño del sistema

- Diseño arquitectónico.
- Diseño de estructuras de datos.
- Diseño de módulos.
- Diseño de lógica difusa.

Fase 3. Desarrollo

- Módulo de usuarios.
- Módulo de inventario.
- Módulo de préstamos.
- Módulo de devoluciones.
- Módulo de reportes.

Fase 4. Pruebas

- Pruebas unitarias.
- Pruebas de integración.
- Corrección de errores.

Fase 5. Implementación y documentación

- Despliegue.
- Manual técnico.
- Manual de usuario.
- Entrega final.

7.2 Cronograma

Actividad.                              |  S1  |   S2     |  S3 |  S4    |  S5  | S6
Levantamiento de requisitos.            | █    | █        |     |        |      | 
Diseño del sistema.                     |      | █        | █   |        |      | 
Desarrollo módulo usuarios.             |      |          | █   | █      |      | 
Desarrollo módulo inventario.           |      |          | █   | █      |      | 
Desarrollo módulo préstamos             |      |          |     | █      | █    | 
Desarrollo módulo reportes.             |      |          |     | █      | █    | 
Pruebas unitarias.                      |      |          |     |        | █    | 
Pruebas de integración.                 |      |          |     |        | █    | 
Corrección de errores.                  |      |          |     |        | █    | █
Documentación y entrega.                |      |          |     |        |      | █

Duración total estimada: 6 semanas.

7.3 Presupuesto del Proyecto

Supuestos

- Equipo de trabajo: 3 estudiantes.
- Inversión total: 50 horas.
- Referencia salarial: 1 SMMLV.

Cálculo

SMMLV 2026: $1.750.905 COP

Horas laborales promedio al mes: 235 horas

Valor hora:

$1.750.905 / 235 = $7.451 COP/hora

Presupuesto

Concepto| Valor
Número de estudiantes| 3
Horas totales del proyecto| 50
Valor hora práctica| $7.451 COP
Mano de obra estimada| $372.550 COP

Resumen financiero

Concepto| Valor (COP)
Mano de obra práctica estudiantil| $372.550
Herramientas de desarrollo| $0
Licenciamiento| $0
'''
 **Plan de Versionado**
'''

# ==============================================================================
# 8. PLAN DE VERSIONADO — PRESTAUDEA
# ==============================================================================
# En cumplimiento con los requerimientos del Trabajo Final de Algoritmia y
# Programación de la Universidad de Antioquia (Profesora Cindy Estrada).
#
# Este módulo documenta el avance incremental del software y sus procedimientos
# relevantes medidos en días transcurridos desde el inicio del proyecto.
# Metodología de control de versiones adoptada: Semantic Versioning (vMAJOR.MINOR.PATCH)
# ==============================================================================


'''
# ==============================================================================
# RESUMEN METODOLÓGICO DE HITOS DE AVANCE
# ==============================================================================
# 1. FASE INICIAL (Días 1 a 10) - Fundamentos del Sistema:
#    El enfoque inicial fue garantizar la persistencia de datos requerida para el
#    problema de 'MJ'. Se estructuró el almacenamiento JSON para evitar la pérdida
#    de información y se blindó la aplicación mediante validaciones de tipos de datos.
#
# 2. FASE INTERMEDIA (Días 11 a 22) - Lógica de Negocio y Transaccionalidad:
#    El software evolucionó hacia una herramienta interactiva mediante menús de consola.
#    Se integraron las entidades permitiendo que los usuarios hicieran préstamos y
#    afectaran la disponibilidad de inventario en tiempo real.
#
# 3. FASE AVANZADA (Días 23 a 32) - Automatización, Reportes y Cierre:
#    El tramo final se centró en resolver las penalizaciones por mora superiores a un mes
#    (facturas con impuesto por conchudez) y en proporcionar valor administrativo
#    mediante reportes en consola y exportación de hojas de cálculo legibles (CSV).
# ==============================================================================
'''
Infraestructura| $0
Costo Total del Proyecto| $372.550
