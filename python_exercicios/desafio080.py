# Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #Teste se for o primeiro valor (c == 0) ou n for maior do que o último valor da lista (lista[-1])
        lista.append(n)         # Adiciona n na última posição da lista
        print('Adicionado ao final da lista...')
    else:
        pos = 0 # Variável pos na primeira posição
        while pos < len(lista): #Laço posição for menor que a quantidade de itens na lista (len(lista)
            if n <= lista[pos]: #Teste se n for menor ou igual a valor na lista na posição (lista[pos])
                lista.insert(pos, n) #Inserir n na lista na posição pos
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}.')
