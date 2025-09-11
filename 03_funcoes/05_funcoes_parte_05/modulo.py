# Importar biblioteca
import math
import os

# Funções 
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def primeiro_grau(a, b):
    x = -b/a
    return x

def segundo_grau(a, b, c):
    if a != 0:
        delta = (b**2)-(4*a*c)
        if delta > 0:
            x1 = (-b+math.sqrt(delta))/(2*a)
            x2 = (-b-math.sqrt(delta))/(2*a)
            yield f"x' = {x1}"
            yield f'x" = {x2}'
        elif delta == 0:
            yield "Não há raizes reais para x."
        else:
            x = -b/(2*a)
            yield x
    else:
        yield primeiro_grau(b, c                                                                                                       )