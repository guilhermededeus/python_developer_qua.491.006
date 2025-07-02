try:    
    arquivo = input("Informe o nome do arquivo: ").strip().lower()
    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    print(texto)

    novo_texto = input("Digite o novo texto: ")
    
    with open(f"{arquivo}.txt", "w", encoding="utf=8") as f:
        f.write(novo_texto)

except Exception as e:
    print(f"Não foi possível atualizar o arquivo. {e}.")
