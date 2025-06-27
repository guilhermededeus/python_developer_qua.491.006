# Dicionario 
usuario = {
    'nome': 'Ana',
    'idade': 25,
    'email': 'maria@gmail.com',
    'profissao': 'Desenvolvedora',
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

# Usuario informa a chave que deseja alterar
chave = input("\nInforme a chave que deseja alterar: ").strip().lower()

# Usuário informa o valor da chave
if chave in usuario:
    usuario[chave] = input(f"Informe o novo valor para {chave}: ").strip()
else:
    print(f"A chave '{chave}' não existe no dicionário.")

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")