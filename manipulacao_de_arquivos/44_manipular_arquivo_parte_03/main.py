import os

while True:
    try:
        novo_texto = input("Digite o texto: ")
        nome_arquivo = input("Informe o nome do arquivo: ").strip().lower()
        with open(f"44_manipular_arquivo_parte_03/{nome_arquivo}.txt", "w", encoding="utf=8") as f:
            f.write(novo_texto)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{nome_arquivo}.txt gravado com sucesso.")
        while True:
            prosseguir = input("Deseja gravar" \
            " outro arquivo? [S]im / [N]ão: ").strip().lower()
            if prosseguir == "s" or prosseguir == "n":
                break
            
            else:
                print("Opção inválida.")
                continue
        match prosseguir:
            case "s":
                continue
            case "n":
                print("Finalizando o programa...")
                break
    except Exception as e:
        print(f"Não foi possível gravar o arquivo. {e}.")
        continue