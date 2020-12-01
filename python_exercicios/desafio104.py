# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(msg):
    ok = False #Declara o ok como Falso para validação no break do Loop While quando Verdadeiro
    valor = 0 #Declara o valor para receber o input
    while True:
        n = str(input(msg))
        if n.isnumeric(): #Teste se o valor é numérico. Quando é omitido o teste lógico é igual a True. Nesse caso, se n é numérico igual a True.
            valor = int(n)
            ok = True # ok recebe True para quebrar o loop na linha 16.
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok: # Omitido o teste lógico, pressupõe que ok seja igual a True
            break
    return valor #Retorna o resultado da função


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')