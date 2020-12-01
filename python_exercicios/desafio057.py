# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o seu sexo: [M/F] ')).upper().strip()[0] #[] fatiamento para pegar a primeira letra.
    if sexo != 'M' and sexo != 'F':
        print('Dados inválidos. Favor, digite "M" para masculino ou "F" para feminino.')
print('Sexo {} registrado com sucesso.'.format(sexo))
