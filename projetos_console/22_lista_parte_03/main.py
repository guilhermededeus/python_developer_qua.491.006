# Lista
cidades = [
    "Brasília",
    "São Paulo",
    "Rio de Janeiro",
    "Teresina",
    "Belo Horizonte",
    "Palmas"
]

for i in range(len(cidades)):
    print(f"índice {i}: {cidades[i]}")
    
# Tratamento de exceção
try:
    # Usuário informa o nome da nova cidade
    nova_cidade = input("Informe o nome da nova cidade: ").strip().title()
    i = int(input("Informe a posição da lita onde deseja inserir: "))
    
    if i >= 0 and i < len(cidades):
        # Insere novo item em uma posição na lista
        cidades.insert(i, nova_cidade)
        print("Cidade inserida com sucesso!")
        ...
    else:
        print("Índice inválido.")
except Exception as e:
    print(f"Não foi possível inserir item na lista. {e}.")
finally:
    # Re-exibe a lista e suas posições
    for i in range(len(cidades)):
        print(f"Índice {i}: {cidades[i]}")