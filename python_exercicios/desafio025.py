#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.title()))
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))