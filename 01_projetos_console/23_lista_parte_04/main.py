# Lista.
cidades = [
    "Brasília",
    "Goiânia",
    "Curitiba",
    "Florianópolis",
    "São Paulo",
    "Rio de Janeiro"
    "Brasília",
    "Teresina",
    "São Paulo",
    "Florianópolis"
    "Brasília",
]

# Usuário informa o nome da cidade a ser pesquisada.
cidade_pesquisada = input("Informe o nome da cidade: ").title().strip()

# Programa conta quanats vezes ocorre o item pesquisado.
qtd = cidades.count(cidade_pesquisada)

# Programa indica quantas vezes o item foi encontrado.
print(f"{cidade_pesquisada} foi encontrada {qtd} vezes na lista.")