"""
# TODO - Crie um programa que receba de um professor vários notas de alunos de 0 a 10 (Não importa qunatas notas). 
Ao final do programa, a média deverá ser calculada e informada, e em seguida, o programa irá informar se o aluno:
- Foi aprovado, caso média for maior ou igual a 7
- Ficou de recuperação, caso média for entre 5 e 7 
- Foi reprovado por nota menor que 5
"""

import os

os.system("cls" if os.name == "nt" else "clear")
notas = []

while True:

    print(f"{"-=-"*2} SISTEMA DE NOTAS {"-=-"*2} ")
    print(f"[1] VER NOTAS")
    print(f"[2] ADICIONAR NOTA")
    print(f"[3] REMOVER NOTA")
    print(f"[4] VER MÉDIA DAS NOTAS")
    print(f"[5] ENCERRAR PROGRAMA")
    print(f"{"-=-"*10}")

    try:
        opcao = input("Operação desejada: ")
        os.system("cls" if os.name == "nt" else "clear")
    
        match opcao:
            case "1":
                try:
                    if not notas:
                        print("Nenhuma nota cadastrada.\n")
                        continue
                    else:
                        for i in range(len(notas)):
                            print(f"Índice {i} - {notas[i]}")
                except Exception as e:
                    print(f"Não foi possível exibir as notas. {e}.\n")
            case "2":
                try:
                    nova_nota = float(input("Nota: "))
                
                    if nova_nota >=0 and nova_nota <=10:
                        os.system("cls" if os.name == "nt" else "clear")
                        notas.append(nova_nota)
                        print("Nota inserida com sucesso!\n")
                    else:
                        print("Nota inválida.")
                except Exception as e:
                    print(f"Não foi possível inserir a nota. {e}.\n")
            case "3":
                try:
                    for i in range(len(notas)):
                        print(f"Índice {i}: {notas[i]}")
                    
                    i = int(input("Informe a posição da nota na lista: "))
                    if i >= 0 and i < len(notas):
                        del(notas[i])
                        print("Nota excluída com sucesso!")
                    else:
                        print("Posição inválida.")
                except Exception as e:
                    print(f"Não foi possível remover a nota. {e}.\n")

            case "4":
                try:
                    media = sum(notas) / len(notas)
                    print(f"Média: {media:.2f}")
                    if media >= 7:
                    
                        print("Aluno aprovado!\n")
                    elif media >= 5:
                        print("Aluno está de recuperação!\n")
                    else:
                        print("Aluno está reprovado!\n")
                except Exception as e:
                    print("Não foi possível calcular a média. {e}.")
            case "5":
                print("Programa encerrado.")
                break

            case _:
                print("Operação inválida.\n")
                continue
            
    except Exception as e:
        print("Não foi executar o programa. {e}.")
