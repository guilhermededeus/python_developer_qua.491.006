# Função 
def mostrar_msg(nome):
    return f"Seja bem vindo, {nome}!"

# Programa principal
nome = input("Informe seu nome: ").strip().title()
 
print(mostrar_msg(nome))