from modulo import traduzir_texto, abrir_arquivo

def main():
    while True:
        print("Seja bem-vindo ao conversor de textos para o Português-BR.\n")
        try:
            # Usuário escolhe o arquivo para traduzir
            arquivo = input("Informe o nome do arquivo que deseja traduzir: ").strip().lower()

            # Lê o conteúdo do arquivo
            with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
                conteudo = f.read()

            # Traduz o conteúdo
            texto_traduzido = traduzir_texto(conteudo)

            # Usuário escolhe o nome do arquivo para salvar
            nome_arquivo = input("Informe o nome do arquivo para salvar: ").strip().lower()
            caminho_arquivo = f"{nome_arquivo}.txt"

            # Salva o arquivo
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                f.write(texto_traduzido)

            print(f"Arquivo salvo como {caminho_arquivo}")

            # Abre o arquivo automaticamente
            abrir_arquivo(caminho_arquivo)
            break
        except Exception as e:
            print(f"Não foi possível traduzir o arquivo. {e}.")

if __name__ == "__main__":
    main()
