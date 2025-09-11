# Dicionario
dicionario = dict(nome="Guilherme", idade=20, email="guilherme@gmail.com")

for chave in dicionario:
    print(f"{chave.capitalize()}: {dicionario.get(chave)}")