def leiaDinheiro(msg):
    válido = False
    while not válido: #Quando omitido, se considera como True. Nesse caso, enquanto não é True mantém o Loop.
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31m ERRO: \"{entrada}\" é uma preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)


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