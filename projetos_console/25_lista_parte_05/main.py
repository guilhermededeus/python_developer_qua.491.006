# Lista
nomes = [
    "Alex",
    "Fernanda",
    "Alexandre",
    "José",
    "Maria",
    "João",
    "Renata",
    "Ricardo",
    "Jason",
    "Marta"
]

# Exibe a lista
for i in range(len(nomes)):
    print(f"Índice {i}: {nomes[i]}")

# Tratamento de exceção 
try:
    i = int(input("Informe a posição do nome na lista: "))
    if i >= 0 and i < len(nomes):
        # Exclui nome da lista
        del(nomes[i])
        print("Nome excluído com sucesso!")
    else:
        print("Posição inválida.")
except Exception as e:
    print(f"Não foi possível excluir o nome da lista. {e}.")
finally:
    for i in range(len(nomes)):
        print(f"Índice {i}: {nomes[i]}")