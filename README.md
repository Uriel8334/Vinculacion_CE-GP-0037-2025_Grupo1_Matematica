# Proyecto de Vinculación CE-GP-0037-2025 — Matemática (Álgebra) · Grupo 1

Construcción del aula virtual en **Moodle**, paquetes interactivos en **eXeLearning (SCORM 1.2)**, simuladores y bancos de preguntas verificados con **IA generativa** para estudiantes de **3.º de Bachillerato** (*UE Pomasqui* y *UE Mitad del Mundo*).

- **Institución:** Universidad de las Fuerzas Armadas ESPE — Departamento de Ciencias Exactas
- **Código de proyecto:** `CE-GP-0037-2025`
- **Asignatura:** Matemática (Álgebra) — Grupo 1 (Equipo de 2 integrantes)

---

## Estructura del Repositorio

- `docs/guias/` — Guías metodológicas oficiales en Markdown (eXeLearning + IA, Moodle y directrices).
- `docs/insumos/` — Sílabo oficial de Matemática (Álgebra), cronograma Excel y plantillas base `.elpx` / SCORM 1.2.
- `capitulos/` — Desarrollo de paquetes por capítulo (`MAT_Cap01` a `MAT_Cap05`) y borradores por subtítulo.
- `banco-preguntas/` — Archivos `.txt` en formato **Aiken** y solucionarios verificados con software (incluye Prueba Diagnóstica).
- `simuladores/` — Recursos interactivos propios (HTML/JS) o referencias/guías de incrustación (GeoGebra) y retos.
- `evidencias-ia/` — Registro de prompts utilizados, scripts de verificación matemática y bitácora grupal.
- `.agents/rules/` — Reglas compartidas cargadas automáticamente por el asistente de IA para todos los integrantes del grupo.

---

## Estructura de Documentación e Insumos

### 1. Guías Oficiales (reconstruidas y verificadas en Markdown)
- [Guía para estudiantes: sílabo, plantilla eXeLearning y generación con IA](./docs/guias/Guia_Estudiantes_eXeLearning_IA.md) *(incluye diagrama de bloques y las 10 instrucciones listas para copiar `0`–`9`)*.
- [Guía para crear las aulas virtuales en Moodle](./docs/guias/Guia_Aulas_Virtuales_Moodle.md) *(incluye flujo del aula, configuración de curso, banco de preguntas, etiquetas y lista de verificación)*.
- [Directrices oficiales del correo de arranque (Ing. Nury Ortiz MSc.)](./docs/guias/Directrices_Correo_Oficial.md).

### 2. Insumos Base Descargados de Google Drive
- [Silabo_Matematica_Algebra.docx](./docs/insumos/Silabo_Matematica_Algebra.docx) — Fuente única oficial (11 capítulos, 59 subtítulos, 13 simuladores).
- [Cronograma_Vinculacion_Grupo1_CE-GP-0037-2025.xlsx](./docs/insumos/Cronograma_Vinculacion_Grupo1_CE-GP-0037-2025.xlsx) — Planificación de 96 h por estudiante, hitos y hoja *Avance por capítulo*.
- [Plantilla_Capitulo_ESPE.elpx](./docs/insumos/Plantilla_Capitulo_ESPE.elpx) — Plantilla base editable en eXeLearning (página `3.2 MRU` completa como modelo).
- [Plantilla_Capitulo_ESPE_SCORM12.zip](./docs/insumos/Plantilla_Capitulo_ESPE_SCORM12.zip) — Ejemplo de paquete exportado a SCORM 1.2.

### 3. Reglas Compartidas para IA del Equipo
- [.agents/rules/proyecto-vinculacion-matematica.md](./.agents/rules/proyecto-vinculacion-matematica.md) — Reglas que Antigravity carga automáticamente para cualquier integrante del grupo que abra este repositorio.

---

## Mapa de Alcance — Matemática (Álgebra) · Grupo 1

- **Aula base en Moodle:** `CEGP0037-MAT` (*CE-GP-0037-2025 · Refuerzo con IA · Matemática (Álgebra) · 3.º BGU*), grupos separados (*UE Pomasqui* y *UE Mitad del Mundo*).
- **Prueba diagnóstica (pretest):** Cubre los **11 capítulos** del sílabo (mínimo 3 preguntas Aiken verificadas por capítulo = **33 preguntas**).
- **Capítulos asignados al Grupo 1 (Capítulos 1 al 5 — 33 de 59 subtítulos = 56 %):**

| Cap. | Título del capítulo | Lote / Hito | Subtítulos | Enfoque(s) en sílabo | Preguntas Aiken / subt. | Simuladores del capítulo |
| :---: | :--- | :---: | :---: | :--- | :---: | :--- |
| **1** | Lógica matemática y conjuntos | **Piloto** *(4 dic)* | **6** (`1.1`–`1.6`) | Puente a la universidad | 10 *(total: 60)* | `1.1` Constructor de tablas de verdad<br>`1.2` Diagramas de Venn interactivos |
| **2** | El conjunto de los números reales | **Lote 1** *(23 dic)* | **5** (`2.1`–`2.5`) | Profundización | 10 *(total: 50)* | `2.1` Recta numérica de los reales |
| **3** | Expresiones algebraicas, ecuaciones e inecuaciones | **Lote 2** *(22 ene)* | **11** (`3.1`–`3.11`) | Refuerzo (`3.1, 3.2, 3.4, 3.7, 3.8`)<br>Profundización (`3.5, 3.10, 3.11`)<br>Puente (`3.3, 3.6, 3.9`) | 6 *(total: 66)* | `3.1` Laboratorio de polinomios<br>`3.2` Resolvedor gráfico de ecuaciones e inecuaciones |
| **4** | Relaciones y funciones | **Lote 2** *(22 ene)* | **5** (`4.1`–`4.5`) | Refuerzo | 6 *(total: 30)* | `4.1` Explorador de funciones |
| **5** | Funciones algebraicas usuales | **Lote 2** *(22 ene)* | **6** (`5.1`–`5.6`) | Refuerzo | 6 *(total: 36)* | `5.1` Familias de funciones con deslizadores |
| **Total G1** | **5 capítulos (`MAT_Cap01` a `MAT_Cap05`)** | **Cierre: 5 feb** | **33 subtítulos** | — | **242 + 33 diag. = 275** | **7 simuladores** |

*(Los capítulos 6 al 11 corresponden al Grupo 2, aunque sus contenidos básicos sí entran en las 3 preguntas por capítulo de la Prueba Diagnóstica).*
