# 115a Vamos criar um menu em Python, usando modularização.
# 115b Vamos ver como fazer acesso a arquivos usando o Python.
# 115c Vamos finalizar o projeto de acesso a arquivos em Python.

from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #Opção de sair do sistema
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        #Digitou a opção errada
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)