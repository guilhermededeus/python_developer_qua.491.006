# Litsa
itens = [
    "Chocolate",
    "Feijão",
    "Arroz",
    "Macarrão",
    "Biscoito",
    "Ovos",
    "Leite",
    "Frango"
]

# Exibe a lista de compras
for i in range(len(itens)):
    print(f"índice {i}: {itens[i]}")

try:
    # Usuárío informa o índice a ser alterado
    i = int(input("Informe o novo valor a ser alterado: "))

    if i >= 0 and i < (len(itens)):
        itens[i] = input("Informe o novo valor: ").capitalize().strip()
        print("Item alterado com sucesso!") 
    else:
        print("índice inválido.")
except Exception as e:
    print(f"Não foi possível alterar o item da lista. {e}.")
finally:
    for i in range(len(itens)):
        print(f"índice {i}: {itens[i]}")