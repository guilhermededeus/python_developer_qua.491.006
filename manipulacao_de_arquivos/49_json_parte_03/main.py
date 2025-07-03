import json

try:
    # Usuário informa o arquivo
    arquivo = input("Informe o arquivo: ").strip().lower()

    #lê o json e desserializa em um dicionário
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        lista = json.load(f)

    # Aplica as conversões
    for dado in lista:
        dado['altura'] = dado['altura'].replace(",",".")
        dado['altura'] = float(dado['altura'])
        dado['peso'] = float(dado['peso'])

        # Sereializa o dicionário em json e grava o arquivo
        with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=4)

        # Confirmação 
    print("Conversão gravada com sucesso.")
except Exception as e:
    print(f"Não foi possível converter. {e}.")