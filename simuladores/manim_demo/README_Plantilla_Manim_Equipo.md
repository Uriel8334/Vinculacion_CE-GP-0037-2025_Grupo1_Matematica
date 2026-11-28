# Guía y Plantilla Base de Animaciones `Manim` — Equipo Matemática (Grupo 1)

Este documento resume la configuración, paleta visual y estructura en Python usada en [axioma_logica_suite.py](./axioma_logica_suite.py) para que **Uriel (Lógica)** y **Leidy (Conjuntos)** generen videos con **exactamente el mismo diseño visual** aprobado por la docente.

---

## 1. Instalación rápida (sin necesidad de instalar LaTeX pesado)

Requisitos en Windows: **Python 3.10+** y **`ffmpeg`** en el `PATH` (`winget install Gyan.FFmpeg` si no estuviera instalado).

Desde la raíz del repositorio clonado:

```powershell
python -m venv .venv
.\.venv\Scripts\pip.exe install manim sympy
```

---

## 2. Estándar Visual Unificado del Curso

| Elemento | Valor exacto | Uso pedagógico |
| :--- | :--- | :--- |
| **Fondo (`BG_AXIOMA`)** | `#070B14` | Lienzo oscuro principal estilo *Axioma Academy* |
| **Cuadrícula (`GRID_COLOR`)** | `#162238` (`opacity=0.45`) | `NumberPlane` sutil de fondo sin ejes visibles |
| **Cian (`CYAN`)** | `#38BDF8` | Término principal / Conjunto $A$ / Hipótesis |
| **Ámbar (`GOLD`)** | `#FBBF24` | Conectivo u operación activa / Conjunto $B$ |
| **Esmeralda (`EMERALD`)** | `#34D399` | Resultado demostrado / Región solución / Verdadero (`V`) |
| **Coral (`ROSE`)** | `#FB7185` | Negación / Complemento / Contraejemplo / Falso (`F`) |
| **Violeta (`VIOLET`)** | `#A78BFA` | Leyes de transformación (De Morgan, Contrarrecíproco) |
| **Tipografía UI** | `"Segoe UI"` | Títulos, pastillas de leyes y notas en español |
| **Tipografía Matemática** | `"Cambria Math"` | Operadores rectos y **variables en cursiva (`slant="ITALIC"` o `<i>x</i>`)** |

> **Regla importante de la docente:** Toda variable matemática ($p, q, x, n, A, B$) debe ir en **cursiva matemática** (`MarkupText("<i>x</i> ∈ <i>A</i>", font="Cambria Math")` o `Text("x", font="Cambria Math", slant="ITALIC")`) para diferenciarla del texto normal, y en `NumberLine` usar `include_numbers=False` con etiquetas `Text` para no requerir compilador LaTeX externo.

---

## 3. Estructura Base en Python (Lista para Copiar — Incluye Ejemplo de Conjuntos / Venn)

Guarda cualquier nueva escena (por ejemplo `simuladores/manim_demo/conjuntos_venn_demo.py`) siguiendo esta plantilla:

```python
from manim import (
    ORIGIN, UP, DOWN, LEFT, RIGHT, WHITE,
    NumberPlane, RoundedRectangle, Rectangle, Circle, Intersection, Union, Difference,
    CurvedArrow, VGroup, Text, MarkupText,
    FadeIn, FadeOut, Write, Create, ReplacementTransform, Flash, Scene, tempconfig,
)

# 1. Paleta y fuentes unificadas del equipo
BG_AXIOMA = "#070B14"
GRID_COLOR = "#162238"
CYAN = "#38BDF8"
GOLD = "#FBBF24"
EMERALD = "#34D399"
ROSE = "#FB7185"
CARD_BG = "#0F172A"
SLATE = "#94A3B8"

FONT_UI = "Segoe UI"
FONT_MATH = "Cambria Math"


def make_axioma_grid(width=16, height=10):
    return NumberPlane(
        x_range=[-width / 2, width / 2, 1],
        y_range=[-height / 2, height / 2, 1],
        background_line_style={"stroke_color": GRID_COLOR, "stroke_width": 1.2, "stroke_opacity": 0.45},
        axis_config={"stroke_opacity": 0},
    )


def make_pill(text_str, border_col=CYAN, font_size=20):
    txt = Text(text_str, font=FONT_UI, font_size=font_size, weight="BOLD", color=WHITE)
    box = RoundedRectangle(
        corner_radius=0.18,
        width=txt.width + 0.5,
        height=txt.height + 0.28,
        stroke_color=border_col,
        stroke_width=2.2,
        fill_color=CARD_BG,
        fill_opacity=0.95,
    )
    txt.move_to(box.get_center())
    return VGroup(box, txt)


class DemoConjuntosVenn(Scene):
    """Plantilla base 16:9 (60 fps) para Conjuntos (1.4 a 1.6): Diagramas de Venn animados."""

    def construct(self):
        self.camera.background_color = BG_AXIOMA
        self.add(make_axioma_grid(16, 10))

        # 1. Pastilla superior y título con variables en cursiva matemática
        tag = make_pill("ESPE · CAPÍTULO 1 · OPERACIONES CON CONJUNTOS", CYAN, font_size=18).to_edge(UP, buff=0.35)
        formula = MarkupText(
            '<i>A</i> ∩ <i>B</i>  =  { <i>x</i> ∈ <i>U</i>  /  <i>x</i> ∈ <i>A</i>  ∧  <i>x</i> ∈ <i>B</i> }',
            font=FONT_MATH,
            font_size=34,
            color=WHITE,
        ).next_to(tag, DOWN, buff=0.3)

        self.play(FadeIn(tag, shift=DOWN * 0.15), Write(formula), run_time=1.0)

        # 2. Universo U y círculos A y B
        universo = Rectangle(width=7.4, height=4.2, stroke_color=SLATE, stroke_width=2).move_to(DOWN * 0.65)
        lbl_u = MarkupText("<i>U</i>", font=FONT_MATH, font_size=28, color=SLATE).next_to(universo.get_corner(UP + RIGHT), DOWN + LEFT, buff=0.18)

        circ_a = Circle(radius=1.45, stroke_color=CYAN, stroke_width=3.5, fill_color=CYAN, fill_opacity=0.18).move_to(LEFT * 0.9 + DOWN * 0.65)
        circ_b = Circle(radius=1.45, stroke_color=GOLD, stroke_width=3.5, fill_color=GOLD, fill_opacity=0.18).move_to(RIGHT * 0.9 + DOWN * 0.65)
        lbl_a = MarkupText("<i>A</i>", font=FONT_MATH, font_size=32, color=CYAN).next_to(circ_a, UP + LEFT, buff=0.05)
        lbl_b = MarkupText("<i>B</i>", font=FONT_MATH, font_size=32, color=GOLD).next_to(circ_b, UP + RIGHT, buff=0.05)

        self.play(Create(universo), FadeIn(lbl_u), Create(circ_a), Create(circ_b), FadeIn(lbl_a), FadeIn(lbl_b), run_time=1.1)

        # 3. Sombrear dinámicamente la región resultante (Boolean Operations nativas de Manim: Intersection, Union, Difference)
        region_inter = Intersection(circ_a, circ_b, stroke_color=EMERALD, stroke_width=4, fill_color=EMERALD, fill_opacity=0.65)
        nota = make_pill("Solo la región común donde se cumplen A y B a la vez", EMERALD, font_size=19).to_edge(DOWN, buff=0.35)

        self.play(FadeIn(region_inter), Flash(region_inter.get_center(), color=EMERALD), FadeIn(nota, shift=UP * 0.15), run_time=1.0)
        self.wait(1.8)


if __name__ == "__main__":
    # Renderizado directo a 16:9 HD (1280x720, 60 fps) — cambiar a 720x1280 y 9x16 si se desea Short vertical
    with tempconfig({
        "pixel_width": 1280,
        "pixel_height": 720,
        "frame_width": 14.222222,
        "frame_height": 8.0,
        "frame_rate": 60,
        "output_file": "demo_conjuntos_venn_16x9",
    }):
        DemoConjuntosVenn().render()
```

---

## 4. Funciones Nativas de `Manim` Ideales para Conjuntos (`1.4` a `1.6`)

Para la parte de Conjuntos, `Manim` ya trae operaciones geométricas booleanas listas para sombrear cualquier región de Venn en 1 línea:
- **Unión ($A \cup B$):** `Union(circ_a, circ_b, fill_color=EMERALD, fill_opacity=0.6)`
- **Intersección ($A \cap B$):** `Intersection(circ_a, circ_b, fill_color=EMERALD, fill_opacity=0.6)`
- **Diferencia ($A \setminus B$):** `Difference(circ_a, circ_b, fill_color=EMERALD, fill_opacity=0.6)`
- **Complemento ($A^c$):** `Difference(universo, circ_a, fill_color=ROSE, fill_opacity=0.5)`
