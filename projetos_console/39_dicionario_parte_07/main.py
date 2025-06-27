usuario = {
    'nome': 'Guilherme',
    'idade': 20,
    'email': "guilherme@gmail.com",
    'profissao': "programador"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

# Usuário informa a chave que deseja remover
chave = input("\nInforme a chave que deseja remover: ").strip().lower()

# Verifica se a chave existe no dicionário
if chave in usuario:
    # Exlui chave do dicionário
    del usuario[chave]
    print(f"A chave '{chave}' foi removida do dicionário.\n") 
else:
    print(f"A chave '{chave}' não existe no dicionário.\n")

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
