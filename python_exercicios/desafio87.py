# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0,0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
p = tc = 0
mai = []
for l in range(3):
    for c in range(3):
        if matriz[l][c] % 2 == 0:
            p += matriz[l][c]
        if c == 2: #Se for a terceira coluna
            tc += matriz[l][c]
        if l == 1: #Se for a segunda linha
            mai.append(matriz[l][c])
print(f'A soma dos valores pares é {p}.')
print(f'A soma dos valores da terceira coluna é {tc}.')
print(f'O maior valor da segunda linha é {max(mai)}.')
