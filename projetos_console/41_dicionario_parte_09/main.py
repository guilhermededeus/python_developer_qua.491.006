usuarios = [
    {
        'nome': 'Guilherme',
        'idade': 20,
        'email':'guilherme@gmail.com'
    },
    {   'nome': 'Maria',
        'idade': 28,
        'email': 'maria@gmail.com'
    },
    {   'nome': 'João',
        'idade': 22,
        'email': 'joao@gmail.com'
    },
]

# Exibe os valores do dicionário
for usuario in usuarios:
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}")
    print()  # Linha em branco para separar os usuários         
