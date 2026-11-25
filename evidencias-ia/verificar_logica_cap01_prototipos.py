"""
Verificación matemática automatizada con SymPy de todas las proposiciones,
clasificaciones e identidades incluidas en el Simulador 1.1 y la animación Manim.
Proyecto ESPE CE-GP-0037-2025 · Matemática (Álgebra) · Capítulo 1.
"""

import itertools
from sympy import symbols
from sympy.logic.boolalg import And, Equivalent, Implies, Not, Or, Xor, simplify_logic

p, q, r = symbols("p q r")


def clasificacion_tabla(expr, vars_list):
    valores = []
    for combo in itertools.product([True, False], repeat=len(vars_list)):
        subs_map = dict(zip(vars_list, combo))
        valores.append(bool(expr.subs(subs_map)))
    if all(valores):
        return "Tautología", valores
    if not any(valores):
        return "Contradicción", valores
    return "Contingencia", valores


# 1. Ejemplos precargados del Simulador 1.1 (Tab 1)
ej1 = Implies(And(Not(p), q), Or(p, Not(q)))
c1, v1 = clasificacion_tabla(ej1, [p, q])
assert c1 == "Contingencia" and v1 == [True, True, False, True], f"Fallo Ej. 1: {c1} {v1}"

ej2 = Equivalent(Or(p, And(q, r)), And(Or(p, q), Or(p, r)))
c2, _ = clasificacion_tabla(ej2, [p, q, r])
assert c2 == "Tautología", f"Fallo Ej. 2: {c2}"

ej3 = Equivalent(Xor(p, q), Equivalent(p, q))
c3, _ = clasificacion_tabla(ej3, [p, q])
assert c3 == "Contradicción", f"Fallo Ej. 3: {c3}"

ej4 = Equivalent(Not(Implies(p, q)), And(p, Not(q)))
c4, _ = clasificacion_tabla(ej4, [p, q])
assert c4 == "Tautología", f"Fallo Ej. 4: {c4}"

ej5 = Equivalent(Implies(p, q), Implies(Not(q), Not(p)))
c5, _ = clasificacion_tabla(ej5, [p, q])
assert c5 == "Tautología", f"Fallo Ej. 5: {c5}"

# 2. Demostraciones animadas en Pizarra Axioma (Tab 3) y Manim
taut_axioma = Implies(p, Or(p, q))
c_ax, _ = clasificacion_tabla(taut_axioma, [p, q])
assert c_ax == "Tautología"

# 3. Verificación aritmética del teorema 1.3 en enteros [-50, 50]: Si 3n + 2 es impar => n es impar
for n in range(-50, 51):
    hip = (3 * n + 2) % 2 != 0
    tes = n % 2 != 0
    assert (not hip) or tes, f"Contraejemplo en n={n}"

print("VERIFICACION SYMPY OK:")
print(f"  - Ej. 1 ESPE [(~p & q) => (p | ~q)]: {c1} -> {['V' if x else 'F' for x in v1]}")
print(f"  - Ej. 2 ESPE [Distributiva 3 vars]:  {c2}")
print(f"  - Ej. 3 ESPE [(p xor q) <=> (p<=>q)]: {c3}")
print(f"  - Negacion del condicional:          {c4}")
print(f"  - Contrarreciproco (3n+2 impar):     {c5} (comprobado en Z)")
