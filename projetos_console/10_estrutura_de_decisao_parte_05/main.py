import os
os.system("cls")

# Entrada de dados
X = float(input('Informe o valor de X: ').replace(",","."))
Y = float(input('Informe o valor de Y: ').replace(",","."))

# Menu
print(f"{'-'*20} ESCOLHA A OPERAÇÃO {'-'*20}")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print(f"{'-'*60}")

# Usuário escolhe o operador desejado
operador = input("Informe a operação desejada: ").strip() # Elima valores nulos. (Como a barra de espaço)

# Matche case
match operador:
    case "1":
        print(f'A soma dos valores é {X+Y}.')
    case "2":
        print(f'A subtração dos valores é {X-Y}.')
    case "3":
        print(f'A multiplicação dos valores é {X*Y}.')
    case "4":
        print(f'A divisão dos valores é {X/Y}.')
    case _: # Default
        print("Operação inválida.")