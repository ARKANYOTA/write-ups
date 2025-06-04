#!/usr/bin/env sage
from sage.all import ZZ
import pyperclip


while True:
    a = int(input("a:").split(" ")[-1])
    b = int(input("b:").split(" ")[-1])
    c = int(input("c:").split(" ")[-1])
    print(a,b,c)
    # a,b,c = 129748011239318971419419099113380388234, 8314724981232796464104623162815968501622239507789606871315987361933464118508, 624075198444090721826682402815071185511598806447785877595960594893773776783159296194476483502398027735795697852904
    R = ZZ['x']
    x = R.gen()

    # Exemple : polynôme x^3 - 6x^2 + 11x - 6 (racines : 1, 2, 3)
    coeffs = [-a**3-2*c+3*b*a, 3*(a**2-b), -6*a, 6]  # Coefficients de degré 0 à 3
    p = sum(c * x**i for i, c in enumerate(coeffs))
    print(f"Polynôme : {p}")

    # Trouver les racines
    racines = p.roots(multiplicities=False)
    racines.sort()
    result = str(racines).replace(" ", "")[1:-1]
    pyperclip.copy(result)
    print("Racines :", result)
