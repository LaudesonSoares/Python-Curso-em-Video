#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-='*10)
t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
pa = t + r
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        c += 1
        print(pa, end=' ')
        pa += r
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
