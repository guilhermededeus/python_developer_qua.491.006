import os

def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
    
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")