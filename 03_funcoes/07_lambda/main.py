import os
# Função normal
'''def somar(x, y):
    result = x + y
    return result'''

# Função lambda
somar = lambda x, y: x+y
limpar_tela = lambda: os.system("cls" if os.name == "nt" else "clear")

# Algoritimo principal
if __name__ == "__main__":
    try:
        x = int(input("Informe o valor de x: "))
        y = int(input("Informe o valor de y: "))
        result = somar(x, y)
        limpar_tela()
        print(f"O resultado da soma é: {result}")
    except Exception as e:
        print("Não foi possível somar. {e}.")