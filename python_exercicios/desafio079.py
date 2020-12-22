#  Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#  Caso o número já exista lá dentro, ele não será adicionado.
#  No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    num = int(input('Digite um número: '))
    if num in lista:
        print('Valor duplicado!Esse valor não foi adicionado.')
    else:
        print('Valor adicionado com sucesso...')
        c = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if c in 'SN':
            if c == 'N':
                lista.append(num)
                break
            elif c == 'S':
                lista.append(num)
lista.sort()
print(f'Os valores digitados foram {lista}.')
