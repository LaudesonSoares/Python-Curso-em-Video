# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
dados = {}
while True:
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
    dados['ctps'] = str(input('Carteira de Trabalho (0 não tem): '))
    if dados['ctps'] == 0:
        break
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + (35 - (datetime.now().year - dados['contratação']))
    break
print('-='*30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}.')
