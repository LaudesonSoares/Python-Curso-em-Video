# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

while True:
    exp = str(input('Digite uma expressão matemática: '))
    if exp.count('(') != exp.count(')'):
        print('A expressão está incorreta!')
    else:
        print('A expressão está correta!')
        break

# Solução Guanabara
# expr = str(input('Digite a expressão: '))
# pilha = []
# for símb in expr:
#     if símb == '(':
#         pilha.append('(')
#     elif símb == ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break
# if len(pilha) == 0:
#     print('Sua expressão está válida!')
# else:
#     print('Sua expressão está errada!')