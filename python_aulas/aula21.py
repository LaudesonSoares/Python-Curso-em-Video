#Funções - Parte 2

# Interactive Help
help()
'Manual das funções, parâmetros, bibliotecas, etc'
print(input.__doc__)

# docstrings
'String de documentação das funcinalidades do Python'

def contador(i, f, p):
    # Ao incluir 3 aspas duplas abre um "docstring" para detalhamento da função e seus parâmetros
    """
    -> Faz uma contagem e mosta na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: seu retorno
    Função criada por Gustavo Guanabara do Curso em Vídeo
    """
    c=i
    while c<=f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

help(contador)

# Argumentos opcionais
'Os parâmetros opcionais são definidos com uso do = (recebe) zero e pode ser para um ou todos os parâmetros.'
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}.')


somar(3, 2, 5)
somar(8, 4)
somar()

# Escopo de variáveis

'Local onde uma varável vai existir ou não vai existir.' \
'Escopo Local > Dentro da Função' \
'Escopo Global > Dentro do Script.'

def teste():
    x = 8 #Variável Local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#Programa Principal
n = 2 #Variável Global
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}') #Variável Local não é reconhecida pois, está dentro da função

-----------------------------------------------------------------------------------------
#A variável pode ter a mesma definição Local e Global, no exemplo abaixo n1 está local na função e global no programa.
def funcao():
    global n1 #Ao chamar 'global' a variável Local assume o valor da variável Global
    n1 = 4 #Variável Local
    print(f'N1 dentro vale {n1}')


n1 = 2 #Variável Global
funcao()
print(f'N1 fora vale {n1}')

# Retorno de resultados
'Retorna o resultado da função com valores, strings, tuplas, listas, dicionários, etc sendo possível criar novas variáveis'
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s #Retorna o valor s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus cáluculos deram {r1}, {r2} e {r3}.')

# AULA PRÁTICA

def fatorial(num=1):
    return 1 + sum(range(num, 0, -1))


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

------------------------------------------------------

def par(n=0):
    return n % 2 == 0


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
