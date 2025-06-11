import os
os.system("cls")

# Declaração de variáveis
Nome = input('Nome: ')
Idade = int(input('Idade: '))

# ternário
result = "é maior de idade." if Idade >= 18 else "é menor de idade."

# saída 
print(f'{Nome} {result}')









