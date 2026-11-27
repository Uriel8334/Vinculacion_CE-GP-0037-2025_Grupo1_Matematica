# Protocolo de Prompts Reutilizables y Ejecución Aislada con Subagentes

> **Proyecto:** `CE-GP-0037-2025` · Matemática (Álgebra) — Grupo 1  
> **Propósito (Regla 8, Parte C de la Guía de Estudiantes):** *«Guardar las instrucciones que funcionaron en un documento del grupo, para que todos las reutilicen y el grupo 2 las herede».*

---

## 1. Metodología de Trabajo para Generar Contenidos con Trazabilidad Real

Para que cada subtítulo, banco de preguntas, simulador y animación cuente con un **prompt puro, reproducible y auditable** (independiente de la charla de coordinación general), aplicaremos este flujo de 4 pasos:

1. **Redacción del Prompt Oficial en Limpio:** Se completa la plantilla oficial (`0` a `9` de [Guia_Estudiantes_eXeLearning_IA.md](../docs/guias/Guia_Estudiantes_eXeLearning_IA.md)) con los datos exactos del sílabo (`Silabo_Matematica_Algebra.docx`) y se guarda en `evidencias-ia/prompts-ejecutados/`.
2. **Ejecución en Subagente Aislado (Contexto Cero):** El prompt exacto se envía a un **subagente nuevo y aislado**, de modo que su salida provenga únicamente de ese prompt (igual que si cualquier docente o integrante del Grupo 2 lo pegara en una sesión limpia de Claude, Gemini o ChatGPT).
3. **Verificación Matemática con Software (`SymPy` / Python) y Bibliografía ESPE:** Todo cálculo, tabla o clave `ANSWER:` de Aiken pasa por script de verificación y contraste con los PDFs guía de la ESPE.
4. **Registro de Ajustes Humanos:** Se documenta qué ajuste pedagógico o tipográfico se aplicó sobre el borrador de la IA antes de subirlo a eXeLearning / Moodle.

---

## 2. Prompts Base Probados que Funcionaron (Fase de Simuladores y Videos — Cap. 1)

Estos dos prompts ya están calibrados con las observaciones de la docente del `25 nov 2026` y sirven directamente para que **Leidy los adapte a Conjuntos (`1.4`–`1.6`)** y para los siguientes capítulos:

### Prompt Reutilizable A — Simulador Interactivo HTML5 sin Conexión (eXeLearning / Moodle)

```text
Actúa como desarrollador educativo de Ingeniería en Software (ESPE) y docente de Matemática para 3.º de Bachillerato de Ecuador (Proyecto CE-GP-0037-2025).

Construye un simulador interactivo autocontenido en un único archivo HTML5 (HTML + CSS + JS puro, sin librerías externas que requieran internet, peso menor a 80 KB) para el tema:
- Capítulo: [n – título exacto del sílabo]
- Simulador del sílabo: [n.k – nombre exacto]
- Instrucción "El estudiante": [copiar del sílabo]
- Instrucción "Reto": [copiar del sílabo]

Requisitos obligatorios de calidad y formato:
1. Tipografía matemática estilo LaTeX: toda letra de variable matemática (p, q, r, x, n, k) debe renderizarse en fuente serif cursiva (<var class="mv">), diferenciada del texto normal y de constantes/operadores rectos.
2. Notación oficial ESPE: usar valores V/F y simbología exacta del material guía ESPE. Prohibido adelantar temas de capítulos posteriores (no incluir ecuaciones cuadráticas ni inecuaciones en el Capítulo 1).
3. Estructura didáctica por pestañas:
   - Pestaña 1: Construcción paso a paso completa visible por defecto + conmutador a "Modo Reto" donde el estudiante predice resultados antes de comprobar y recibe retroalimentación específica por error.
   - Pestaña 2: Intuición visual manipulable (diagramas SVG interactivos con colores claros).
   - Pestaña 3: Explorador visual de propiedades/leyes del tema.
4. Pie de autoría obligatorio en la esquina inferior derecha:
   "© Desarrollado por: Uriel Andrade & Leidy Saraguro · Ing. en Software ESPE · Proyecto CE-GP-0037-2025" (sin datos personales de estudiantes ni colegios).
```

### Prompt Reutilizable B — Cápsula Visual Animada en Python (`Manim 60 fps`)

```text
Actúa como programador de animaciones matemáticas en Python con Manim Community (v0.22+) al estilo visual de Axioma Academy / 3Blue1Brown para estudiantes de 3.º de Bachillerato (ESPE · Proyecto CE-GP-0037-2025).

Genera una escena animada a 60 fps sobre fondo oscuro (#070B14) con cuadrícula tenue NumberPlane (#162238) para explicar visualmente:
- Subtítulo del sílabo: [n.k – nombre exacto]
- Ejercicio / propiedad a demostrar: [enunciado simple sin temas adelantados]

Reglas técnicas y visuales:
1. Evitar bloques estáticos de texto: mostrar transformaciones dinámicas con CurvedArrow, ReplacementTransform, resaltados Indicate/Flash y representación gráfica/geométrica sincronizada (circuitos, recta numérica o diagramas de Venn coloreados por regiones).
2. Diferenciar visualmente las variables matemáticas (en cursiva serif) respecto de las etiquetas explicativas en español neutro.
3. Mantener cada paso con su etiqueta breve de justificación/ley aplicada y verificar que ningún elemento rebase los márgenes del lienzo.
```

---

## 3. Cómo Ubicar los Videos de Refuerzo en Moodle vs. eXeLearning

Según [Guia_Aulas_Virtuales_Moodle.md](../docs/guias/Guia_Aulas_Virtuales_Moodle.md) y la reunión docente del `25 nov 2026`:

- **Estructura fija de cada sección de capítulo en Moodle (7 elementos):**
  1. `Capítulo n: <título>` (Área de texto y medios)
  2. `n · Material de estudio` (Paquete SCORM 1.2 de eXeLearning / Libro)
  3. `n · Tutor IA del capítulo`
  4. `n · Ejercicios de práctica`
  5. `n.k · Simulador: <nombre>`
  6. `n · Evaluación en línea`
  7. `n · Foro de dudas`
- **¿Dónde van las cápsulas de video hechas en Python (`Manim`)?**
  - **En etapa de revisión con la docente (sección oculta en Moodle):** En una carpeta/recurso de apoyo (`1 · Material audiovisual de refuerzo — Lógica`) para revisión directa sin salir del aula.
  - **En versión final para estudiantes de colegio (baja conectividad):** La lista de verificación de Moodle indica *«videos enlazados, no subidos»*; por tanto, una vez aprobados por la docente, pueden alojarse como *No listados* en YouTube e insertarse mediante enlace ligero dentro del bloque `Lo que debes saber` / `Ejemplo resuelto` de eXeLearning o como recurso `URL` de apoyo.
