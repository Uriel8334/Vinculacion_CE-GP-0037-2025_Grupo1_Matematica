# Análisis Resumido de Alcance y Profundidad — Capítulo 1 (Parte Lógica: `1.1` a `1.3`)

> **Proyecto:** `CE-GP-0037-2025` · Matemática (Álgebra) · 3.º BGU (*UE Pomasqui* y *UE Mitad del Mundo*)  
> **Responsable de esta mitad:** Uriel Andrade (`1.1`, `1.2`, `1.3` + `Simulador 1.1`)  
> **Compañera (segunda mitad):** Leidy Saraguro (`1.4`, `1.5`, `1.6` — Conjuntos + `Simulador 1.2`)  
> **Enfoque oficial en el Sílabo:** **Puente a la universidad** (`class="enfoque enf-puente"` — *el colegio no lo cubre a profundidad; se explica desde cero con prerrequisitos y ejemplos paso a paso*).

---

## 1. Cruce entre el Sílabo Oficial y el Material Guía ESPE (`1_Logica_Matematica.pdf`)

| Subtítulo exacto del Sílabo | Qué trae el PDF oficial ESPE (`Tema 1`, 29 págs.) | Nivel y recorte pedagógico para 3.º BGU | Tarea autónoma y ejercicios clave |
| :--- | :--- | :--- | :--- |
| **`1.1` Proposiciones: definición, conectivos lógicos, tablas de verdad** | • Secc. `1.2`: Proposiciones simples/atómicas y compuestas (`V`, `F`), y expresiones que **no** son proposiciones (preguntas, exclamaciones, ecuaciones abiertas como \(x+3=5\)).<br>• Secc. `1.3`: Los **6 conectivos ESPE**: básicos (\(\neg, \wedge, \vee\)) y compuestos (\(\underline{\vee}, \Rightarrow, \Leftrightarrow\)), con antecedente/hipótesis y consecuente/tesis.<br>• Secc. `1.4`: Tablas de verdad de 2 y 3 variables; clasificación en **Tautología**, **Contradicción** y **Contingencia**.<br>• Secc. `1.5.1`: Leyes fundamentales (De Morgan, condicional \(p \Rightarrow q \equiv \neg p \vee q\), negación del condicional \(\neg(p \Rightarrow q) \equiv p \wedge \neg q\), contrarrecíproco). | • **Mantener intacta la simbología ESPE:** valores `V`/`F`, flechas dobles \(\Rightarrow, \Leftrightarrow\) y disyunción exclusiva \(\underline{\vee}\) (*«ó»*).<br>• **Aterrizar con intuición visual:** explicar cada conectivo con situaciones cotidianas de Quito y analogía de interruptores/flujo de agua.<br>• **No saturar** con simplificaciones algebraicas de 15 pasos (como el ej. 2 de pág. 14 del PDF); limitar simplificaciones con leyes a 3–5 pasos claros tipo examen de ingreso.<br>• *Corrección detectada:* en pág. 5 del PDF dice \(x-1 \neq 1\) para el dominio de \(\sqrt{\frac{x+3}{x-1}}\); debe corregirse a \(x-1 \neq 0\). | *Tarea autónoma `1.1`:* Memoriza tablas de verdad.<br>• Identificar proposiciones vs. no proposiciones.<br>• Evaluar tablas de verdad y hallar valores desconocidos sabiendo que una expresión es tautología o falsa (ej. \(p \Rightarrow q \equiv F\)). |
| **`1.2` Funciones proposicionales, uso de cuantificadores** | • Secc. `1.7`: Diferencia entre enunciado abierto \(P(x): x+3=7,\; x \in \mathbb{R}\) y proposición cerrada.<br>• Secc. `1.7.1`: Cuantificador universal (\(\forall\), *«para todo»*) y existencial (\(\exists\), *«existe al menos un»*).<br>• Secc. `1.7.2`: Reglas de negación de cuantificadores:<br>\(\neg[\forall x \in A: P(x)] \equiv \exists x \in A: \neg P(x)\)<br>\(\neg[\exists x \in A: P(x)] \equiv \forall x \in A: \neg P(x)\). | • Empezar probando \(P(x)\) sobre **conjuntos numéricos finitos pequeños** (p. ej. \(A=\{1,2,3,4\}\)) para que el estudiante compruebe elemento por elemento cuándo \(\forall\) falla con un solo contraejemplo y cuándo \(\exists\) basta con un acierto.<br>• *Ajuste ético/pedagógico:* reemplazar los ejemplos de la pág. 26 del PDF por ejemplos académicos y cotidianos respetuosos (transporte en el Metro de Quito, múltiplos, propiedades geométricas o notas de colegio). | *Tarea autónoma `1.2`:* Construye proposiciones a partir de funciones proposicionales.<br>• Traducir de lenguaje común a simbólico con \(\forall, \exists\), determinar su valor de verdad (`V`/`F`) y escribir su negación correcta. |
| **`1.3` Métodos de demostración: directo e indirecto** | • Secc. `1.3.5` y `1.5.1`: Estructura de un teorema (\(H \Rightarrow T\)), recíproco y **contrarrecíproco** (\(\neg T \Rightarrow \neg H\)).<br>• Secc. `1.5.3`: Demostración algebraica de tautologías sin tabla de verdad.<br>• Secc. `1.6`: Reglas de inferencia (*Modus Ponens*, *Modus Tollens*, silogismo hipotético y falacia de afirmar el consecuente).<br>• *Faltante en el PDF:* método indirecto por **reducción al absurdo** (\(H \wedge \neg T \Rightarrow \text{Contradicción}\)). | • **Recortar exceso de reglas de inferencia:** en vez de memorizar 9 nombres en latín, enfocarse en las dos esenciales que sustentan las demostraciones (*Modus Ponens* = base del método directo; *Modus Tollens* / contrarrecíproco = base del indirecto).<br>• **Completar con bibliografía del sílabo** (*Castillo, Navas & Toro* / *Lara & Arroba*) el método de **reducción al absurdo**, aplicado a propiedades sencillas de números pares/impares y divisibilidad que un estudiante de 3.º BGU entiende sin dificultad. | *Tarea autónoma `1.3`:* Identifica métodos de demostración.<br>•Dado un teorema sencillo (p. ej. *«Si \(3n+2\) es impar, entonces \(n\) es impar»*), elegir y ordenar los pasos por método directo, contrarrecíproco o reducción al absurdo, y detectar falacias comunes. |

---

## 2. Comparativa Técnica de Propuestas Visuales (HTML/JS vs. Python `Manim`)

Como aún no tenemos acceso al Moodle de prueba para verificar límites de subida o iframes externos, preparamos **ambos prototipos funcionales** para revisarlos con la docente:

| Criterio | Prototipo A: Simulador + Pizarra Animada en HTML5/JS | Prototipo B: Video Animado con `Manim` (Python) |
| :--- | :--- | :--- |
| **Archivo generado** | [simulador_1_1_logica_tablas_verdad.html](../../simuladores/simulador_1_1_logica_tablas_verdad.html) | [animacion_logica_axioma.mp4](../../simuladores/manim_demo/animacion_logica_axioma.mp4) *(código en [animacion_logica_axioma.py](../../simuladores/manim_demo/animacion_logica_axioma.py))* |
| **Peso aproximado** | **~35 KB** (ultraligero, ideal para baja conectividad) | **~300 KB – 2 MB** por ejercicio corto en MP4 |
| **Funciona sin internet dentro de `.elpx` / SCORM** | **Sí, 100 % offline** (idéntico al modelo `simulador_cinematica_1d.html` de Física) | Si va dentro del SCORM suma peso; la guía de Moodle recomienda **enlazar videos** (p. ej. YouTube *No listado*) |
| **Interactividad del estudiante** | **Alta:** el alumno cambia interruptores/válvulas, arma fórmulas, predice `V`/`F`, comprueba su reto y avanza/retrocede cada paso a su ritmo | **Pasiva (video):** excelente impacto visual estilo *Axioma Academy* / Shorts para explicar un ejemplo clave en 30–45 segundos |
| **Recomendación para nuestro Capítulo 1** | **Usarlo como `Simulador 1.1` oficial incrustado en eXeLearning** (cumple el reto del sílabo + la idea de circuitos/agua de la docente + pizarra paso a paso) | **Usarlo para 1 cápsula corta por subtítulo** (`1.1`, `1.2`, `1.3`) alojada en canal de YouTube *No listado* y enlazada como apoyo visual |

---

## 3. Plan de Producción Inmediato para Lógica (`1.1` a `1.3`)

1. **Validar con la docente hoy en la tarde:**
   - El recorte pedagógico de la tabla superior (`1.1`, `1.2`, `1.3`).
   - El prototipo interactivo HTML (`Simulador 1.1` con 3 pestañas: *Constructor y Reto de Tablas/Cuantificadores*, *Circuito Eléctrico / Flujo de Agua* y *Pizarra Animada estilo Axioma*).
   - El video corto compilado en Python con **`Manim`** para decidir si también generamos cápsulas animadas enlazadas.
2. **Siguiente paso tras el visto bueno:**
   - Redactar y verificar con `SymPy` los **5 bloques de eXeLearning** y las **10 preguntas Aiken** de `1.1`, luego `1.2` y luego `1.3` (30 preguntas verificadas en total para tu mitad del Capítulo 1), mientras Leidy avanza `1.4`–`1.6` y el `Simulador 1.2` de Diagramas de Venn.
