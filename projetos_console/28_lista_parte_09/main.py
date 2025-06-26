# Importação
import os

# Lista
nomes = ["Fulano", "Ciclano", "Beltrano", "João", "Maria", "José"]

# Exibe a lista
print(f"{"-=-"*2} LISTA {"-=-"*2} ")
for i in range(len(nomes)):
    print(f"Índice: {i} - {nomes[i]}")
print(f"{"-=-"*6}")

try:

    i = int(input("Informe o índice que deseja separar: "))
    if i >= 0 and i < (len(nomes)):
        nome_isolado = nomes.pop(i)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{nome_isolado} separdo com sucesso!")
        
        # Lista exibe os valores sem o item isolado
        print(f"{"-=-"*2} LISTA {"-=-"*2} ")
        for i in range(len(nomes)):
            print(f"Índice: {i} - {nomes[i]}")
        print(f"{"-=-"*6}")

        # Exibe o item isolado
        print(f"Item isolado da lista: {nome_isolado}")
    else:
        print("índice inválido.")
    
except Exception as e:
    print(f"Não foi possível executar a operação. {e}.")
