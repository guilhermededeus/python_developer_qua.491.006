import os
os.system("cls")

Nome = input("Digite seu nome: ")
Idade = int(input("Digite sua idade: "))
Altura = float(input("Digite sua altura em metros: ").replace(",","."))

print(f"Seja bem-vindo {Nome}!")
print(f"Idade do usuário: {Idade}.")
print(f"Altura do usuário: {Altura}.")

print(f"{Nome}: {type(Nome)}.")
print(f"{Idade}: {type(Idade)}.")
print(f"{Altura}: {type(Altura)}.")
