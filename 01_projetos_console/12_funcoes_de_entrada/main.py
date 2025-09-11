import os
os.system("cls")

# Entrada de dados.
Nome = input("Informe seu nome: ").title() # Primeiro caractere de cada palavra fica em maiúscula.
print(f"Seu nome é: {Nome}.")

Texto = input("Digite uma frase: ").capitalize() # Somente a primeira a letra da primeira palavra fica em maiúscula.
print(f"Frase: {Texto}.")

Minuscula = input("Digite um texto em minúscula: ").upper() # Todas as letras ficarão em maiúscula.
print(f"Texo em maiúscula: {Minuscula}")

Maiuscula = input("Digite um texto em maiúscula: ").lower() # Todas as letras ficarão em minúscula.
print(f"Texo em minúscula: {Maiuscula}")


