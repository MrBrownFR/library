"""Module avec toutes les fonctions et constantes que j'utilise pour des
opérations et qui ne sont pas dans les modules classiques"""

from cmath import *
from math import *

# FIXME : remplacer toutes les variables par des majuscules

def dis(a, b, c):
    """Calcule le discriminant d'une fonction carrée. Elle prend les 3 variables de Delta en 
    paramètres, dans l'ordre a, b et c."""
    delta = b**2 - 4 * a * c
    return (delta)

def n_sol(a, b, c):
    """Renvoie le nombre de racines d'une fonction du second degré."""
    d = dis(a, b, c)
    if d > 0:
        return ('2 solutions réelles')
    elif d == 0:
        return ('1 solution réelles')
    elif d < 0:
        return ('pas de solutions réelles')

def sol(a, b, c):
    """Renvoie les solutions d'une équation du second degré, en accord avec
    le discriminant."""
    delta = dis(a, b, c)
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        solutions = [x1, x2]
    elif delta == 0:
        x0 = -b / 2 * a
        solutions = [x0]
    elif delta < 0:
        z1 = (-b - 1j * sqrt(-delta)) / 2 * a
        z2 = (-b + 1j * sqrt(-delta)) / 2 * a
        solutions = [z1, z2]
        return (solutions, delta)

def can(a, b, c):
    """Renvoie la forme canonique d'une équation du decond degré."""
    alpha = -(b / (2 * a))
    beta = a * (alpha**2) + b * alpha + c
    return ("f(x) =" + "%a(x-%alpha)+%beta" + ", avec alpha =" + alpha
            + "et bêta =" + beta)


if __name__ == "__main__":
    print("! ATTENTION: CE SCRIPT A ETE CONCU COMME UNE LIBRAIRIE ET NON PAS COMME UN EXECUTABLE !"
    "\nCE PROGRAMME N'EXECUTERA AUCUNE INSTRUCTION.")
