import json 

try:
    arquivo = input("Informe o nome do arquivo: ").strip().lower()

    #lê o json e desserializa em um dicionário
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    # output
    print(f"\n{"-=-"*5} DADOS {"-=-"*5}\n")
    for dado in dados:
        for chave in dado:
            print(f"{chave.capitalize()}: {dado.get(chave)}")
        print (f"\n{"-=-"*20}\n")
except Exception as e:
    print ("Não foi possivel ler o arquivo json.")