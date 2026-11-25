r"""
Prototipo de animación matemática estilo Axioma Academy / 3Blue1Brown usando Manim.
Proyecto de Vinculación ESPE CE-GP-0037-2025 · Matemática (Álgebra) · Capítulo 1 (Lógica).

Tema demostrado (Subtítulo 1.1 - Enfoque Puente a la universidad):
    Demostración paso a paso de la Negación del Condicional:
        ¬(p ⇒ q)  ≡  p ∧ ¬q
    y verificación visual en la tabla de verdad ESPE (V / F).

Ejecución:
    .\.venv\Scripts\manim.exe -qm simuladores\manim_demo\animacion_logica_axioma.py NegacionDelCondicional
"""

from manim import (
     ORIGIN,
    UP,
    DOWN,
    LEFT,
    RIGHT,
     BLACK,
    WHITE,
     RoundedRectangle,
    SurroundingRectangle,
    Line,
    VGroup,
    Text,
    FadeIn,
    FadeOut,
    Write,
    TransformMatchingShapes,
    ReplacementTransform,
    Create,
    Indicate,
    Scene,
    config,
)

# Estilo visual oscuro tipo Axioma Academy (16:9 HD para aula virtual; adaptable a 9:16 Shorts)
BG_DARK = "#0B101E"
CYAN = "#38BDF8"
GOLD = "#FBBF24"
EMERALD = "#34D399"
ROSE = "#FB7185"
SLATE = "#94A3B8"
FONT_MAIN = "Segoe UI"
FONT_MATH = "Cambria Math"


class NegacionDelCondicional(Scene):
    def construct(self):
        self.camera.background_color = BG_DARK

        # 1. Encabezado del capítulo
        tag = Text(
            "ESPE · Matemática (Álgebra) · Cap. 1: Lógica Matemática",
            font=FONT_MAIN,
            font_size=20,
            color=SLATE,
        ).to_edge(UP, buff=0.35)

        titulo = Text(
            "¿Cómo se niega realmente un condicional  p ⇒ q ?",
            font=FONT_MAIN,
            font_size=32,
            weight="BOLD",
            color=WHITE,
        ).next_to(tag, DOWN, buff=0.22)

        linea_sep = Line(LEFT * 5.8, RIGHT * 5.8, color="#1E293B", stroke_width=2).next_to(
            titulo, DOWN, buff=0.18
        )

        self.play(FadeIn(tag, shift=DOWN * 0.2), Write(titulo), Create(linea_sep), run_time=1.3)

        # 2. Mostrar el error frecuente primero
        error_lbl = Text(
            "Error frecuente:   ¬(p ⇒ q)  ≠  ¬p ⇒ ¬q",
            font=FONT_MATH,
            font_size=27,
            color=ROSE,
        ).next_to(linea_sep, DOWN, buff=0.35)
        self.play(FadeIn(error_lbl, shift=UP * 0.15), run_time=0.9)
        self.wait(0.9)
        self.play(FadeOut(error_lbl), run_time=0.5)

        # 3. Desarrollo algebraico paso a paso con leyes ESPE
        paso0 = Text("¬( p ⇒ q )", font=FONT_MATH, font_size=44, color=CYAN).move_to(
            UP * 1.15 + LEFT * 2.2
        )
        ley0 = self._badge("Expresión a simplificar", CYAN).next_to(paso0, RIGHT, buff=0.8)

        self.play(Write(paso0), FadeIn(ley0, shift=LEFT * 0.2), run_time=1.0)
        self.wait(0.7)

        paso1 = Text("≡  ¬( ¬p ∨ q )", font=FONT_MATH, font_size=42, color=GOLD).next_to(
            paso0, DOWN, buff=0.48, aligned_edge=LEFT
        )
        ley1 = self._badge("Equivalencia del condicional: (p ⇒ q) ≡ (¬p ∨ q)", GOLD).next_to(
            paso1, RIGHT, buff=0.55
        )
        self.play(FadeIn(paso1, shift=DOWN * 0.2), FadeIn(ley1, shift=LEFT * 0.2), run_time=1.1)
        self.play(Indicate(paso1, color=GOLD, scale_factor=1.05), run_time=0.7)
        self.wait(0.7)

        paso2 = Text("≡  ¬(¬p)  ∧  ¬q", font=FONT_MATH, font_size=42, color=WHITE).next_to(
            paso1, DOWN, buff=0.48, aligned_edge=LEFT
        )
        ley2 = self._badge("Ley de De Morgan: cambia ∨ por ∧", CYAN).next_to(
            paso2, RIGHT, buff=0.55
        )
        self.play(FadeIn(paso2, shift=DOWN * 0.2), FadeIn(ley2, shift=LEFT * 0.2), run_time=1.1)
        self.wait(0.7)

        paso3 = Text("≡  p  ∧  ¬q", font=FONT_MATH, font_size=46, color=EMERALD).next_to(
            paso2, DOWN, buff=0.52, aligned_edge=LEFT
        )
        ley3 = self._badge("Ley de Involución: ¬(¬p) ≡ p", EMERALD).next_to(
            paso3, RIGHT, buff=0.55
        )
        caja_res = SurroundingRectangle(paso3, color=EMERALD, buff=0.18, corner_radius=0.12)

        self.play(
            Write(paso3),
            Create(caja_res),
            FadeIn(ley3, shift=LEFT * 0.2),
            run_time=1.2,
        )
        self.wait(1.2)

        # 4. Transición limpia a comprobación en Tabla de Verdad ESPE (V / F)
        bloque_pasos = VGroup(paso0, ley0, paso1, ley1, paso2, ley2, paso3, ley3, caja_res)
        resumen_arriba = Text(
            "Identidad demostrada:   ¬(p ⇒ q)   ≡   p ∧ ¬q",
            font=FONT_MATH,
            font_size=32,
            color=EMERALD,
        ).next_to(linea_sep, DOWN, buff=0.32)

        self.play(ReplacementTransform(bloque_pasos, resumen_arriba), run_time=0.9)

        headers = ["p", "q", "p ⇒ q", "¬(p ⇒ q)", "p ∧ ¬q"]
        rows_data = [
            ["V", "V", "V", "F", "F"],
            ["V", "F", "F", "V", "V"],
            ["F", "V", "V", "F", "F"],
            ["F", "F", "V", "F", "F"],
        ]

        tabla_group = VGroup()
        col_x = [-4.2, -2.6, -0.7, 1.5, 3.8]

        hdr_vg = VGroup()
        for cx, h in zip(col_x, headers):
            t = Text(h, font=FONT_MATH, font_size=26, weight="BOLD", color=CYAN).move_to(
                [cx, 0.75, 0]
            )
            hdr_vg.add(t)
        tabla_group.add(hdr_vg)

        row_vgs = VGroup()
        for r_idx, row in enumerate(rows_data):
            y = 0.05 - r_idx * 0.65
            rv = VGroup()
            for c_idx, (cx, val) in enumerate(zip(col_x, row)):
                col = EMERALD if (r_idx == 1 and c_idx >= 3) else (ROSE if val == "F" and c_idx >= 3 else WHITE)
                t = Text(val, font=FONT_MATH, font_size=25, color=col).move_to([cx, y, 0])
                rv.add(t)
            row_vgs.add(rv)
        tabla_group.add(row_vgs)

        self.play(FadeIn(hdr_vg, shift=DOWN * 0.15), run_time=0.6)
        for rv in row_vgs:
            self.play(FadeIn(rv, shift=RIGHT * 0.15), run_time=0.35)

        destaque_fila2 = SurroundingRectangle(
            row_vgs[1], color=GOLD, buff=0.14, corner_radius=0.08
        )
        nota_final = Text(
            "Único caso verdadero: cuando la hipótesis p es V y la tesis q es F.",
            font=FONT_MAIN,
            font_size=22,
            color=GOLD,
        ).to_edge(DOWN, buff=0.38)

        self.play(Create(destaque_fila2), FadeIn(nota_final, shift=UP * 0.15), run_time=1.0)
        self.wait(2.2)

    def _badge(self, text: str, border_color: str) -> VGroup:
        lbl = Text(text, font=FONT_MAIN, font_size=19, color=WHITE)
        box = RoundedRectangle(
            corner_radius=0.14,
            width=lbl.width + 0.42,
            height=lbl.height + 0.26,
            stroke_color=border_color,
            stroke_width=1.8,
            fill_color="#131B2E",
            fill_opacity=0.95,
        )
        lbl.move_to(box.get_center())
        return VGroup(box, lbl)
