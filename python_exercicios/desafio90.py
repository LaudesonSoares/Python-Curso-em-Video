# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dados = {}
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
if dados['média'] >= 7:
     dados['situação'] = 'Aprovado'
elif 5 <= dados['média'] < 7:
    dados['situação'] = 'Recuperação'
else:
     dados['situação'] = 'Reprovado'
print('-='*30)
for k, v in dados.items():
    print(f'- {k} é igual a {v}')
