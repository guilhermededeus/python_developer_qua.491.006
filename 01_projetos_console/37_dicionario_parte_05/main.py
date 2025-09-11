# Dicionario
usuario = {
    'nome': 'Maria',
    'idade': 28,
    'email': 'maria@gmail.com',
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

# Adcionando nova chave
usuario['profissao'] = input("Informe a profissão: ").strip()

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

