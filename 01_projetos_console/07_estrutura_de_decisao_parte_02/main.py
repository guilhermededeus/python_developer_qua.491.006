import os
os.system("cls")

# Declaração de variáveis
Nome = input('Informe seu nome: ')
Idade = int(input('Informe sua idade: '))
Altura = float(input('Informe sua altura: ').replace(",","."))

# Estruta de decisão
if Idade >= 18 and Altura >= 1.15:
        print(f'{Nome} tem permissão para acessar o brinquedo.')
else: 
    print(f'{Nome} não tem permissão para acessar o brinquedo.')