chaves = ("Nome", "Idade", "Email", "Telefone", "Profissão")

usuario = {
    chaves[0]: "Guilherme",
    chaves[1]: 20,
    chaves[2]: "guilherme@gmail.com",
    chaves[3]: "99999-9999",
    chaves[4]: "Programador"
}

for chave in usuario:
    print(f"{chave}: {usuario.get(chave)}")