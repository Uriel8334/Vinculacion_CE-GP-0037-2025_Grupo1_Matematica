r"""
Suite de Animaciones Matemáticas en Python con Manim (Estilo Axioma Academy / 3Blue1Brown).
Proyecto de Vinculación ESPE CE-GP-0037-2025 · Matemática (Álgebra) · Capítulo 1 (Lógica 1.1 a 1.3).

Incluye 2 videos complementarios a 60 FPS:
1. ShortAxiomaDeMorganYCircuito (Formato Vertical 9:16 YouTube Shorts, 1080x1920, 60fps):
   - Subtítulo 1.1: Transformación animada de ¬(p ⇒ q) ≡ p ∧ ¬q con salto curvo de De Morgan,
     rotación física de 180° del operador ∨ -> ∧, aniquilación por destello de doble negación ¬¬,
     y simulación inferior de corriente eléctrica en un circuito en serie que enciende un foco.
2. CapsulaCuantificadoresYDemostracion (Formato Horizontal 16:9 Aula Virtual, 1280x720, 60fps):
   - Subtítulos 1.2 y 1.3: Negación visual de cuantificadores con recta numérica animada y
     cruce espacial de Hipótesis/Tesis en una demostración indirecta por Contrarrecíproco.
"""

import numpy as np
from manim import (
     PI,
    ORIGIN,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    UL,
    UR,
    DL,
    DR,
    WHITE,
    NumberPlane,
    NumberLine,
    RoundedRectangle,
    SurroundingRectangle,
    Circle,
    Dot,
    Line,
    Arrow,
    CurvedArrow,
    VGroup,
    Text,
    FadeIn,
    FadeOut,
    Write,
    Create,
    GrowFromCenter,
    Transform,
    ReplacementTransform,
    Rotate,
    Indicate,
    Flash,
    MoveAlongPath,
    Scene,
    rate_functions,
)

BG_AXIOMA = "#070B14"
GRID_COLOR = "#162238"
CYAN = "#38BDF8"
GOLD = "#FBBF24"
EMERALD = "#34D399"
ROSE = "#FB7185"
VIOLET = "#A78BFA"
SLATE = "#94A3B8"
CARD_BG = "#0F172A"

FONT_UI = "Segoe UI"
FONT_MATH = "Cambria Math"


def make_axioma_grid(width=20, height=20):
    plane = NumberPlane(
        x_range=[-width / 2, width / 2, 1],
        y_range=[-height / 2, height / 2, 1],
        background_line_style={
            "stroke_color": GRID_COLOR,
            "stroke_width": 1.2,
            "stroke_opacity": 0.45,
        },
        axis_config={"stroke_opacity": 0},
    )
    return plane


def make_pill(text_str, border_col=CYAN, font_size=22):
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


class ShortAxiomaDeMorganYCircuito(Scene):
    """Escena vertical 9:16 (configurar pixel_width=1080, pixel_height=1920, frame_width=9, frame_height=16)."""

    def construct(self):
        self.camera.background_color = BG_AXIOMA
        grid = make_axioma_grid(12, 20)
        self.add(grid)

        # Encabezado superior estilo Short educativo
        chip = make_pill("ESPE · LÓGICA MATEMÁTICA 1.1", CYAN, font_size=20).move_to(UP * 6.8)
        titulo = Text(
            "¿Cómo se niega una promesa\nlógica  p ⇒ q ?",
            font=FONT_UI,
            font_size=34,
            weight="BOLD",
            color=WHITE,
            line_spacing=0.9,
        ).next_to(chip, DOWN, buff=0.35)

        self.play(FadeIn(chip, shift=DOWN * 0.2), Write(titulo), run_time=1.0)

        # Zona central de ecuación dinámica
        eq_y = UP * 2.9
        t_neg_ext = Text("¬", font=FONT_MATH, font_size=64, color=ROSE)
        t_lp = Text("(", font=FONT_MATH, font_size=62, color=SLATE)
        t_p = Text("p", font=FONT_MATH, font_size=62, color=CYAN)
        t_imp = Text("⇒", font_size=58, font=FONT_MATH, color=GOLD)
        t_q = Text("q", font=FONT_MATH, font_size=62, color=CYAN)
        t_rp = Text(")", font=FONT_MATH, font_size=62, color=SLATE)

        eq_step1 = VGroup(t_neg_ext, t_lp, t_p, t_imp, t_q, t_rp).arrange(RIGHT, buff=0.22).move_to(eq_y)
        law_card = make_pill("1. Reescribir el condicional:  (p ⇒ q) ≡ (¬p ∨ q)", GOLD, font_size=19).move_to(
            UP * 1.35
        )

        self.play(Write(eq_step1), run_time=0.9)
        self.wait(0.4)
        self.play(FadeIn(law_card, shift=UP * 0.15), Indicate(VGroup(t_p, t_imp, t_q), color=GOLD), run_time=0.8)

        # Transformar (p => q) en (¬p v q)
        t_neg_p_in = Text("¬p", font=FONT_MATH, font_size=62, color=CYAN)
        t_or = Text("∨", font=FONT_MATH, font_size=58, color=GOLD)
        t_q2 = Text("q", font=FONT_MATH, font_size=62, color=CYAN)
        inner_or = VGroup(t_neg_p_in, t_or, t_q2).arrange(RIGHT, buff=0.28).move_to(
            VGroup(t_p, t_imp, t_q).get_center()
        )

        self.play(
            t_lp.animate.next_to(inner_or, LEFT, buff=0.18),
            t_rp.animate.next_to(inner_or, RIGHT, buff=0.18),
            t_neg_ext.animate.shift(LEFT * 0.22),
            ReplacementTransform(VGroup(t_p, t_imp, t_q), inner_or),
            run_time=0.9,
        )
        self.wait(0.4)

        # Paso 2: Salto de De Morgan con flechas curvas y rotación de 180° de ∨ -> ∧
        law_card2 = make_pill("2. Ley de De Morgan: entra ¬ y gira  ∨ → ∧", CYAN, font_size=19).move_to(
            UP * 1.35
        )
        arc1 = CurvedArrow(
            t_neg_ext.get_top() + UP * 0.1,
            t_neg_p_in.get_top() + UP * 0.12,
            angle=-0.85,
            color=ROSE,
            stroke_width=3.5,
        )
        arc2 = CurvedArrow(
            t_neg_ext.get_top() + UP * 0.1,
            t_q2.get_top() + UP * 0.12,
            angle=-0.65,
            color=ROSE,
            stroke_width=3.5,
        )

        self.play(ReplacementTransform(law_card, law_card2), Create(arc1), Create(arc2), run_time=0.85)

        t_dbl_neg = Text("¬(¬p)", font=FONT_MATH, font_size=58, color=GOLD)
        t_and = Text("∧", font=FONT_MATH, font_size=58, color=EMERALD)
        t_neg_q = Text("¬q", font=FONT_MATH, font_size=60, color=CYAN)
        eq_step2 = VGroup(t_dbl_neg, t_and, t_neg_q).arrange(RIGHT, buff=0.35).move_to(eq_y)

        # Rotamos visualmente ∨ 180 grados mientras muta a ∧
        self.play(
            FadeOut(VGroup(t_neg_ext, t_lp, t_rp, arc1, arc2)),
            ReplacementTransform(t_neg_p_in, t_dbl_neg),
            Rotate(t_or, angle=PI),
            ReplacementTransform(t_q2, t_neg_q),
            run_time=0.95,
        )
        t_and.move_to(t_or.get_center())
        self.remove(t_or)
        self.add(t_and)
        self.wait(0.35)

        # Paso 3: Ley de Involución ¬(¬p) -> p con destello Flash
        law_card3 = make_pill("3. Ley de Involución:  ¬(¬p) ≡ p", EMERALD, font_size=20).move_to(
            UP * 1.35
        )
        t_p_final = Text("p", font=FONT_MATH, font_size=66, color=EMERALD)
        t_and_final = Text("∧", font=FONT_MATH, font_size=62, color=EMERALD)
        t_neg_q_final = Text("¬q", font=FONT_MATH, font_size=66, color=EMERALD)
        eq_final = VGroup(t_p_final, t_and_final, t_neg_q_final).arrange(RIGHT, buff=0.35).move_to(eq_y)

        self.play(
            ReplacementTransform(law_card2, law_card3),
            Flash(t_dbl_neg.get_center(), color=GOLD, line_length=0.35, num_lines=12),
            ReplacementTransform(t_dbl_neg, t_p_final),
            ReplacementTransform(t_and, t_and_final),
            ReplacementTransform(t_neg_q, t_neg_q_final),
            run_time=0.9,
        )
        box_res = SurroundingRectangle(eq_final, color=EMERALD, buff=0.24, corner_radius=0.16, stroke_width=3)
        self.play(Create(box_res), run_time=0.5)

        # Zona inferior: Circuito en Serie animado (Intuición física de p ∧ ¬q)
        sub_circ = Text(
            "Intuición con Circuito en Serie (p = V,  q = F ⇒ ¬q = V)",
            font=FONT_UI,
            font_size=21,
            weight="BOLD",
            color=GOLD,
        ).move_to(DOWN * 0.35)

        circ_card = RoundedRectangle(
            corner_radius=0.22,
            width=7.9,
            height=4.2,
            stroke_color="#1E293B",
            stroke_width=2,
            fill_color="#0B1324",
            fill_opacity=0.92,
        ).move_to(DOWN * 2.85)

        y_wire = -2.95
        w1 = Line([-3.3, y_wire, 0], [-1.9, y_wire, 0], color=GOLD, stroke_width=5)
        sw1 = Line([-1.9, y_wire, 0], [-0.9, y_wire + 0.55, 0], color=ROSE, stroke_width=5)
        w2 = Line([-0.9, y_wire, 0], [0.2, y_wire, 0], color=SLATE, stroke_width=5)
        sw2 = Line([0.2, y_wire, 0], [1.2, y_wire + 0.55, 0], color=ROSE, stroke_width=5)
        w3 = Line([1.2, y_wire, 0], [2.45, y_wire, 0], color=SLATE, stroke_width=5)

        lbl_sw1 = Text("p = V", font=FONT_MATH, font_size=26, color=EMERALD).move_to([-1.4, y_wire + 1.0, 0])
        lbl_sw2 = Text("¬q = V", font=FONT_MATH, font_size=26, color=EMERALD).move_to([0.7, y_wire + 1.0, 0])

        dots_sw = VGroup(
            Dot([-1.9, y_wire, 0], radius=0.08, color=WHITE),
            Dot([-0.9, y_wire, 0], radius=0.08, color=WHITE),
            Dot([0.2, y_wire, 0], radius=0.08, color=WHITE),
            Dot([1.2, y_wire, 0], radius=0.08, color=WHITE),
        )

        bulb = Circle(radius=0.48, stroke_color=SLATE, stroke_width=4, fill_color="#1E293B", fill_opacity=1).move_to(
            [2.95, y_wire, 0]
        )
        bulb_txt = Text("F", font=FONT_MATH, font_size=28, weight="BOLD", color=SLATE).move_to(bulb.get_center())

        self.play(
            FadeIn(sub_circ),
            FadeIn(circ_card),
            Create(VGroup(w1, sw1, w2, sw2, w3)),
            FadeIn(dots_sw),
            FadeIn(VGroup(lbl_sw1, lbl_sw2, bulb, bulb_txt)),
            run_time=0.9,
        )
        self.wait(0.55)

        # Cerrar ambos interruptores en serie
        sw1_closed = Line([-1.9, y_wire, 0], [-0.9, y_wire, 0], color=EMERALD, stroke_width=6)
        sw2_closed = Line([0.2, y_wire, 0], [1.2, y_wire, 0], color=EMERALD, stroke_width=6)
        self.play(
            Transform(sw1, sw1_closed),
            Transform(sw2, sw2_closed),
            w2.animate.set_color(GOLD),
            w3.animate.set_color(GOLD),
            run_time=0.75,
        )

        # Pulso eléctrico recorriendo el circuito y encendiendo la salida V
        full_path = Line([-3.3, y_wire, 0], [2.45, y_wire, 0])
        pulse = Dot([-3.3, y_wire, 0], radius=0.14, color=GOLD)
        bulb_on = Circle(
            radius=0.48, stroke_color=GOLD, stroke_width=5, fill_color="#FEF08A", fill_opacity=1
        ).move_to(bulb.get_center())
        bulb_txt_on = Text("V", font=FONT_MATH, font_size=30, weight="BOLD", color="#713F12").move_to(
            bulb.get_center()
        )

        self.play(MoveAlongPath(pulse, full_path, rate_func=rate_functions.ease_in_out_sine), run_time=0.9)
        self.remove(pulse)
        self.play(
            Transform(bulb, bulb_on),
            Transform(bulb_txt, bulb_txt_on),
            Flash(bulb.get_center(), color=GOLD, line_length=0.42, num_lines=14),
            run_time=0.65,
        )

        cierre = Text(
            "Solo se refuta p ⇒ q cuando se cumple p (V)\ny al mismo tiempo falla q (F).",
            font=FONT_UI,
            font_size=22,
            color=WHITE,
            line_spacing=0.9,
        ).move_to(DOWN * 6.05)
        self.play(FadeIn(cierre, shift=UP * 0.2), run_time=0.7)
        self.wait(1.8)


class CapsulaCuantificadoresYDemostracion(Scene):
    """Escena horizontal 16:9 HD para incrustar/enlazar en Aula Virtual (Subtítulos 1.2 y 1.3)."""

    def construct(self):
        self.camera.background_color = BG_AXIOMA
        grid = make_axioma_grid(16, 10)
        self.add(grid)

        # ==================== PARTE A: CUANTIFICADORES (1.2) ====================
        tag1 = make_pill("SUBTÍTULO 1.2 · CUANTIFICADORES Y SU NEGACIÓN", CYAN, font_size=18).to_edge(
            UP, buff=0.35
        )
        self.play(FadeIn(tag1, shift=DOWN * 0.15), run_time=0.6)

        t_neg = Text("¬ [", font=FONT_MATH, font_size=48, color=ROSE)
        t_quant = Text("∀x ∈ ℝ :", font=FONT_MATH, font_size=48, color=CYAN)
        t_pred = Text("x + 3 = 7", font=FONT_MATH, font_size=48, color=GOLD)
        t_close = Text("]", font=FONT_MATH, font_size=48, color=ROSE)
        prop_q = VGroup(t_neg, t_quant, t_pred, t_close).arrange(RIGHT, buff=0.25).move_to(UP * 1.45)

        self.play(Write(prop_q), run_time=1.0)

        a1 = CurvedArrow(
            t_neg.get_top() + UP * 0.08,
            t_quant.get_top() + UP * 0.1,
            angle=-0.7,
            color=ROSE,
            stroke_width=3,
        )
        a2 = CurvedArrow(
            t_neg.get_top() + UP * 0.08,
            t_pred.get_top() + UP * 0.1,
            angle=-0.55,
            color=ROSE,
            stroke_width=3,
        )
        regla_q = Text(
            "Cambia ∀ por ∃  y  niega la condición (= pasa a ≠)",
            font=FONT_UI,
            font_size=23,
            color=SLATE,
        ).move_to(UP * 0.35)

        self.play(Create(a1), Create(a2), FadeIn(regla_q), run_time=0.85)

        res_quant = Text("∃x ∈ ℝ :", font=FONT_MATH, font_size=52, color=EMERALD)
        res_pred = Text("x + 3 ≠ 7", font=FONT_MATH, font_size=52, color=EMERALD)
        prop_neg = VGroup(res_quant, res_pred).arrange(RIGHT, buff=0.3).move_to(UP * 1.45)

        self.play(
            FadeOut(VGroup(t_neg, t_close, a1, a2)),
            ReplacementTransform(t_quant, res_quant),
            ReplacementTransform(t_pred, res_pred),
            Flash(res_quant.get_center(), color=EMERALD, line_length=0.28),
            run_time=0.95,
        )

        # Recta numérica probando un contraejemplo real (etiquetas con Text sin depender de LaTeX)
        nl = NumberLine(
            x_range=[-1, 6, 1],
            length=8.5,
            color=SLATE,
            include_numbers=False,
        ).move_to(DOWN * 1.25)
        nl_nums = VGroup(
            *[
                Text(str(k), font=FONT_MATH, font_size=22, color=SLATE).next_to(
                    nl.n2p(k), DOWN, buff=0.18
                )
                for k in range(-1, 7)
            ]
        )

        tracker_dot = Dot(nl.n2p(4), radius=0.14, color=ROSE)
        eval_lbl = Text(
            "Con x = 4:  4 + 3 = 7 (no cumple ≠ 7)", font=FONT_UI, font_size=22, color=ROSE
        ).next_to(nl, DOWN, buff=0.68)

        self.play(Create(nl), FadeIn(nl_nums), GrowFromCenter(tracker_dot), FadeIn(eval_lbl), run_time=0.85)
        self.wait(0.5)

        eval_ok = Text(
            "Con x = 1:  1 + 3 = 4 ≠ 7   ⇒   ¡Basta un x para que ∃ sea Verdadera (V)!",
            font=FONT_UI,
            font_size=22,
            weight="BOLD",
            color=EMERALD,
        ).next_to(nl, DOWN, buff=0.68)

        self.play(
            tracker_dot.animate.move_to(nl.n2p(1)).set_color(EMERALD),
            ReplacementTransform(eval_lbl, eval_ok),
            Flash(nl.n2p(1), color=EMERALD, line_length=0.3),
            run_time=1.0,
        )
        self.wait(1.1)

        # Limpiar para Parte B
        self.play(
            FadeOut(VGroup(tag1, prop_neg, regla_q, nl, nl_nums, tracker_dot, eval_ok)),
            run_time=0.6,
        )

        # ==================== PARTE B: MÉTODO INDIRECTO / CONTRARRECÍPROCO (1.3) ====================
        tag2 = make_pill(
            "SUBTÍTULO 1.3 · DEMOSTRACIÓN INDIRECTA (CONTRARRECÍPROCO)", VIOLET, font_size=18
        ).to_edge(UP, buff=0.35)
        self.play(FadeIn(tag2, shift=DOWN * 0.15), run_time=0.5)

        box_h = make_pill("p :  3n + 2 es impar", CYAN, font_size=26)
        arrow_imp = Text("⇒", font=FONT_MATH, font_size=50, color=GOLD)
        box_t = make_pill("q :  n es impar", GOLD, font_size=26)
        teorema_dir = VGroup(box_h, arrow_imp, box_t).arrange(RIGHT, buff=0.45).move_to(UP * 1.55)

        self.play(FadeIn(box_h, shift=RIGHT * 0.2), Write(arrow_imp), FadeIn(box_t, shift=LEFT * 0.2), run_time=0.9)

        swap_top = CurvedArrow(
            box_t.get_top() + UP * 0.06,
            box_h.get_top() + UP * 0.06,
            angle=0.55,
            color=VIOLET,
            stroke_width=3,
        )
        swap_bot = CurvedArrow(
            box_h.get_bottom() + DOWN * 0.06,
            box_t.get_bottom() + DOWN * 0.06,
            angle=0.55,
            color=VIOLET,
            stroke_width=3,
        )
        nota_swap = Text(
            "Contrarrecíproco: intercambiamos posición y negamos ambos lados (¬q ⇒ ¬p)",
            font=FONT_UI,
            font_size=21,
            color=VIOLET,
        ).move_to(UP * 0.2)

        self.play(Create(swap_top), Create(swap_bot), FadeIn(nota_swap), run_time=0.85)

        box_nq = make_pill("¬q :  n es par", EMERALD, font_size=26).next_to(arrow_imp, LEFT, buff=0.45)
        box_np = make_pill("¬p :  3n + 2 es par", EMERALD, font_size=26).next_to(arrow_imp, RIGHT, buff=0.45)

        self.play(
            FadeOut(VGroup(swap_top, swap_bot)),
            ReplacementTransform(box_t, box_nq),
            ReplacementTransform(box_h, box_np),
            run_time=1.0,
        )

        # Desarrollo algebraico limpio en 3 pasos
        alg1 = Text("Si n es par  ⇒  n = 2k   (k ∈ ℤ)", font=FONT_MATH, font_size=32, color=WHITE).move_to(
            DOWN * 0.85
        )
        alg2 = Text(
            "3n + 2  =  3(2k) + 2  =  6k + 2", font=FONT_MATH, font_size=34, color=CYAN
        ).next_to(alg1, DOWN, buff=0.35)
        alg3 = Text(
            "=  2(3k + 1)   ⇒   ¡Múltiplo de 2 (PAR)!   [Demostrado]",
            font=FONT_MATH,
            font_size=33,
            color=EMERALD,
        ).next_to(alg2, DOWN, buff=0.38)
        marco_fin = SurroundingRectangle(alg3, color=EMERALD, buff=0.16, corner_radius=0.12)

        self.play(Write(alg1), run_time=0.8)
        self.play(FadeIn(alg2, shift=UP * 0.15), run_time=0.8)
        self.play(Write(alg3), Create(marco_fin), Flash(alg3.get_center(), color=EMERALD), run_time=1.0)
        self.wait(2.0)
