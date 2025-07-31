import os

def fatorial(n):
    return 1 if n == 0 else n * fatorial(n-1)

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")