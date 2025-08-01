# Importações
import os

# Entrada de dados
while True:
    try: 
        # Usuário informa o nome do arquivo
        arquivo = input("Informe o nome do arquivo: ").strip().lower()

        # Abre o arquivo
        with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
            arquivo_aberto = f.read()
        os.system("cls" if os.name == "nt" else "clear")

        # Mostra os dados do arquivo
        print(arquivo_aberto)
        while True:
            prosseguir = input("Deseja abrir outro arquivo? [S]im / [N]ão: ").strip().lower()
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
        print(f"Não foi possível ler o arquivo. {e}.")
        continue