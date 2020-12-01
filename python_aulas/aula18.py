# Listas dentro de listas

dados = ['Pedro', 25] #Criando uma lista
pessoas = list() #Criando uma lista vazia
pessoas.append(dados[:]) #Adicionando uma lista em outra lista

pessoas = [['Pedro', 25],['Maria', 19], ['João', 32]]
#             0       1     0       1      0      1  Posição dos itens da lista interna
#            -----------   -----------    ----------
#                  0             1             2     Posição da lista interna da lista externa

print(pessoas[0][0]) #Pedro
print(pessoas[1][1]) #19
print(pessoas[2][0]) #João
print(pessoas[1]) #['Maria', 19]

# Exemplos aula prática

#Exemplo 1
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p)
    print(p[0])
    print(f'{p[0]} tem {p[1]} anos de idade.')

#Exemplo 2
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome:'))) #Inserir nome na lista dado
    dado.append(int(input('Idade: '))) #Inserir idade na lista dado
    galera.append(dado[:]) #Criar uma cópia da lista dado na lista galera
    dado.clear() #Limpar os itens da lista dado
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')