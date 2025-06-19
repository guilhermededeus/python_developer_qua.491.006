import os
os.system("cls")

# Lista.
Nomes = ["Fulano","Ciclano","Beltrano","João","Maria","José"]

Nomes.sort(reverse=False) # True para decrecente / False para crescente.

# Imprime a lista.
print(f"Primeiro nome: {Nomes[0]}")
print(f"Quarto nome: {Nomes[3]}")

# Imprime o número de iten na lista.
print(f"Quantidade de itens na lista: {len(Nomes)}")

for Nome in Nomes:
    print(Nome) # Nomes um abaixo do outro: 

print(Nomes.index("Maria")) # Identificar posição do objeto na lista.

for Nome in Nomes:
    print(f"{Nome} - {Nomes.index(Nome)}") # Identificar o nome e posição do objeto na lista.

