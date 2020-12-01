# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list() #lISTA COM TODOS OS DADOS DOS ALUNOS
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media]) #ADICIONA NOME NA POSIÇÃO 0, NA POSIÇÃO 1 NOTA1 E NOTA2 EM UMA NOVA LISTA DENTRO DA LISTA FICHA E
                                                #MEDIA NA POSIÇÃO 2 DA LISTA FICHA. FORMA-SE UMA LISTA COMPOSTA EM 3 NÍVEIS.
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}') #ALINHAMENTOS (:< ESQUERDA) (:> DIREITA) DO TÍTULO
print('-' * 26)
for i, a in enumerate(ficha): #LAÇO PARA EXIBIR O ÍNDICE (i) , NOME E MÉDIA DO ALUNO (a) NA POSIÇÃO [0] e [2]
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1: #O NÚMERO DO ALUNO TEM QUE SER MENOR QUE O TAMANHO DA LISTA FICHA (QUANTIDADE DE ALUNOS CADASTRADOS
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}') #opc É O NÚMERO DO ALUNO E A POSIÇÃO [0] É O NOME NA LISTA FICHA
                                                               # E A POSIÇÃO [1] NA LISTA FICHA SÃO AS NOTAS
print('<<< VOLTE SEMPRE >>>')
