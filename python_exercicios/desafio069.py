#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

maior18 = homem = mulheres20 = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        maior18 +=1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    print('-'*20)
    con = ' '
    while con not in 'SN':
        con = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if con == 'N':
        break
print(f'O total de pessoas com mais de 18: {maior18}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulheres20} mulheres com menos de 20 anos.')
