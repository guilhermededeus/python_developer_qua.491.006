import os
os.system("cls")

# Declaração de variáveis
Nome_Aluno = input('Nome do aluno: ')
Media = float(input('Média de nota: '))

if Media >= 0 and Media <= 10:
    if Media >= 7:
        print(f'{Nome_Aluno} está aprovado!')
    elif Media >= 5:
        print(f'{Nome_Aluno} está em recuperação!')
    else:
        print(f'{Nome_Aluno} está reprovado!')
else:
    print('Nota inválida.')











'''
Nota_1 = float(input('Primeira nota: '))
Nota_2 = float(input('Segunda nota: '))
Nota_3 = float(input('Terceira nota: ')
               
Media = (Nota_1 + Nota_2 + Nota_3) / 3
'''
