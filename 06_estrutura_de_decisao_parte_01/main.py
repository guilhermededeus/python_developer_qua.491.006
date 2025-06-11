import os
os.system("cls")

# Declaração de variáveis
Nome = input('Informe seu nome: ')
Idade = int(input('Informe sua idade: '))

# Estruta de decisão
if Idade >= 18:
        print(f'{Nome} é maior de idade.')
else: 
    print(f'{Nome} é menor de idade.') 