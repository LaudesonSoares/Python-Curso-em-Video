# Listas
#
# Listas são estruturas de variáveis compostas onde múltiplas informações são guardadas em grupo na memória.
# Listas possuem as seguintes características
#
# São definidas por []
# São mutáveis

lanche = ["Hamburger", "Batata", "Cenoura", "Banana"]

print("Imprimindo uma lista inteira")
print(lanche)
print()

#Adicionando elemento em uma lista
lanche = ["Hamburger", "Batata", "Cenoura", "Banana"]

print("Adicionando elemento a uma lista")
lanche.append('Biscoito')
print(lanche)

#Incluindo elemento no meio de uma lista
lanche = ["Hamburger", "Batata", "Cenoura", "Banana"]

print("Incluindo elemento a uma lista")
lanche.insert(0, 'Cachorro quente')
print(lanche)

#Apagando elemento em uma lista
lanche = ["Hamburger", "Batata", "Cenoura", "Banana"]

print("Adicionando elemento a uma lista")
del lanche[3]
print(lanche)

lanche = ["Hamburger", "Batata", "Cenoura", "Banana"]

print("Adicionando elemento a uma lista")
lanche.pop(3)  #Normalmente utilizado pop para apagar o último item
print(lanche)

lanche = ["Hamburger", "Batata", "Cenoura", "Banana"]

print("Adicionando elemento a uma lista")
lanche.remove('Batata')  #Normalmente utilizado pop para apagar o último item
print(lanche)

#Organizando os itens de uma lista

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
print(valores)

#Organizando de forma inversa os itens de uma lista

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort(reverse=True)
print(valores)

#Quantidade de itens em uma lista

valores = [8, 2, 5, 4, 9, 3, 0]
print(len(valores))

#Exemplos Aula Prática

#Exemplo 1
num = [2, 5, 9, 1]
num [2] = 3 #Alterando item em uma lista
num.append(7) #Adicionando item em uma lista
num.sort() #Organizando itens em uma lista
print(num)
num.sort (reverse=True) #Organizando itens
num.insert(2, 2) #Inserindo item na lista. Primeiro a posição (2) e depois o item (2).
num.pop() #Removendo último item da lista
num.pop(2) #Removendo item na posição da lista
num.remove(2) #Removendo item da lista que aparece primeiro na lista
if 4 in num:  #Teste para evitar erro de remoção em item não contido na lista
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.') #Quantidade de itens na lista

#Exemplo 2

#Estrutura de laços

valores = list() #Listas podem ser chamadas pelo comando list ou por []
valores.append(5)
valores.append(9)
valores.append(4)

#Mostrar itens da lista
for v in valores:
    print(f'{v}...', end='')
#Mostrar itens e posição na lista
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

#Adicionar e Mostrar itens e posição na lista
valores = list()
for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

#Interligação entre listas no Python

a = [2, 3, 4, 7]
b = a #Quando igualamos uma lista a outra é criada uma ligação entre as duas listas e qualquer alteração em uma reflete na outra
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#Criando cópia de lista
a = [2, 3, 4, 7]
b = a[:] #Cópia dos valores de A e joga em B
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
