# Dicionario
usuario = {
    'nome': 'Maria',
    'idade': 28,
    'email': 'maria@gmail.com',
    'profissao': 'Designer',
}

# Exibe os valores
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")    