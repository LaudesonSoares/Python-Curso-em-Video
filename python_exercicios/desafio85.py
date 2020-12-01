# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

núm = [[], []] #Criadas duas listas dentro da lista núm
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor) #Lista núm na posição 0 é a lista dos pares
    else:
        núm[1].append(valor) #Lista núm na posição 1 é a lista dos ímpares
núm[0].sort()
núm[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')