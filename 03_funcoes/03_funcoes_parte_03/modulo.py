# Importações
import os

# Funções
def area_quadrado(lado):
    area = lado **2
    return area

def area_retangulo(base, altura):
    area = base * altura
    return area

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
