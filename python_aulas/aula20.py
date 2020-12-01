# Funções

#As funções são rotinas no Python. Exemplos são print, len, input, int, float
#Cria comandos personalizados

def lin(): #função sem parâmetro, com parênteses vazio ()
    print('-' * 30)
#Entre o def e o programa principal deve ter 2 linhas para organizar o código

lin()
print('  CURSO EM VÍDEO  ')
lin()
print('  APRENDA PYTHON  ')
lin()
print('  GUSTAVO GUANABARA  ')
lin()

#----------------------------------------------------------------------
def mensagem(msg): #Ao incluir a 'msg' dentro do parênteses da função cria-se um parâmetro
    print('-' * 30)
    print(msg) #e chamar 'msg' entre a função automatiza a rotina criando o link
    print('-'*30)

mensagem('SISTEMA DE ALUNOS')
#---------------------------------------------------------------------
def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


título('  CURSO EM VÍDEO  ')
título('  APRENDA PYTHON  ')
título('  GUSTAVO GUANABARA  ')

#____________________________________________________________________
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#Programa Principal
soma(4, 5)
soma(a=8, b=9) #Declarando explicitamente o parâmetro
soma(b=2, a=1) #Declarando explicitamente o parâmetro em qualquer ordem
#Precisa explicitar sempre os dois parâmetros ou deixar implícito os dois, caso contrário irá gerar erro.

#Empacotamento de Parâmetros (Tuplas)
def contador(* núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#Empacotamento de Parâmetros (Lista)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
