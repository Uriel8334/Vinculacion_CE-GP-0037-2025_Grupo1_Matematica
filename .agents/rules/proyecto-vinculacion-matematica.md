# Reglas del Proyecto de Vinculación CE-GP-0037-2025 — Matemática (Álgebra)

Este repositorio pertenece al **Grupo 1 de Matemática (Álgebra)** del Proyecto de Vinculación `CE-GP-0037-2025` (*Refuerzo Académico Virtual con IA – 3.º de Bachillerato*, UE Pomasqui y UE Mitad del Mundo, ESPE).

Al generar contenidos, bancos de preguntas, simuladores o paquetes eXeLearning en este proyecto, sigue **sin excepción** estas reglas:

1. **El sílabo manda (`docs/insumos/Silabo_Matematica_Algebra.docx`):**
   - Usa exactamente la numeración y el título de cada capítulo y subtítulo (`n.k`). Prohibido inventar o añadir temas fuera del sílabo sin autorización docente.
   - Respeta el enfoque oficial del sílabo para cada subtítulo:
     - `Refuerzo` (`class="enfoque enf-refuerzo"`): máx. 250 palabras en explicación, 2 ejemplos resueltos.
     - `Profundización` (`class="enfoque enf-prof"`): máx. 450 palabras de básico a avanzado, 3 ejemplos resueltos.
     - `Puente a la universidad` (`class="enfoque enf-puente"`): empieza por prerrequisitos desde cero, máx. 600 palabras, 3 ejemplos paso a paso.

2. **Estructura exacta por subpágina en eXeLearning (`Plantilla_Capitulo_ESPE.elpx`, modelo `3.2 MRU`):**
   - 5 bloques en este orden exacto:
     1. `Lo que debes saber` (inicia con `<span class="enfoque ...">Enfoque: ...</span>` + explicación + 3–5 puntos clave).
     2. `Ejemplo resuelto` (2 o 3 ejemplos; la solución SIEMPRE oculta en el botón de retroalimentación `"Ver solución"`).
     3. `Para recordar` (3 a 5 viñetas cortas con fórmulas e ideas clave).
     4. `Comprueba lo aprendido` (3 preguntas cortas: conceptual, cálculo sencillo, aplicación; respuestas SIEMPRE ocultas en `"Ver respuestas"`).
     5. `Pregúntale al tutor IA` (3 preguntas sugeridas: otro ejemplo, practicar con corrección, "por qué").
   - Eliminar la página `"Guía de esta plantilla (borrar antes de publicar)"` antes de exportar a SCORM 1.2.

3. **Formato matemático LaTeX y estilo lingüístico:**
   - **PROHIBIDO usar el signo `$`** para fórmulas en HTML, Aiken o Moodle.
   - Usa únicamente `\( ... \)` para fórmulas en línea y `\[ ... \]` para fórmulas en bloque.
   - Español neutro con contexto cotidiano de Quito / Ecuador, coma decimal en prosa (`3,6`) y unidades del Sistema Internacional cuando apliquen.
   - Cero datos personales de estudiantes o colegios. Créditos obligatorios en imágenes y simuladores externos (GeoGebra, PhET, H5P).

4. **Verificación obligatoria con software:**
   - Antes de entregar cualquier ejemplo resuelto, ejercicio de `"Comprueba lo aprendido"`, reto de simulador o pregunta Aiken, **ejecuta un script en Python (`sympy` / `numpy`)** para comprobar algebraica y numéricamente que el resultado es exacto y que en opción múltiple existe **una única respuesta correcta**.

5. **Banco de preguntas (formato Aiken + solucionario separado para el docente):**
   - Enunciado en una sola línea (con `\( ... \)`), opciones `A)`, `B)`, `C)`, `D)`, línea `ANSWER: X` y línea en blanco entre preguntas.
   - **Capítulos 1 y 2 (Piloto y Lote 1):** **10 preguntas** por subtítulo (6 práctica + 4 evaluación).
   - **Capítulos 3, 4 y 5 (Lote 2 de Matemática):** **6 preguntas** por subtítulo.
   - **Prueba diagnóstica:** cubre los **11 capítulos** del sílabo (mínimo 3 preguntas por capítulo: 1 fácil, 1 media, 1 difícil = 33 preguntas mínimas).

6. **Nomenclatura de entregables:**
   - Capítulos: `MAT_Cap01_Logica-matematica-y-conjuntos.elpx` + `MAT_Cap01_Logica-matematica-y-conjuntos_SCORM12.zip`.
   - Respaldos parciales por subtítulo: `MAT_CapXX_YYYY-MM-DD.elpx`.
