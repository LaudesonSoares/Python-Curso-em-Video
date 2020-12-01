n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.') #f string faz a interpolação de variável

#Quando for necessário identificar o maior ou menor valor, deve-se incluir um contador e se o contador for 1,
# maior ou menor valor é igual do valor do input. A partir daí faz o teste de hipóteses. Exemplo abaixo:

maior = menor = cont = 0
valor = int(input('Digite um valor: '))
cont += 1
if cont == 1:
    maior = menor = valor
elif valor < menor:
    menor = valor
elif valor > maior:
    maior = valor