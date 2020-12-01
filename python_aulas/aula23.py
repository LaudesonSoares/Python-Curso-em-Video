# #Tratamento de Erros e Exceções (Classe Exception)
#
# Há diferença entre Erros e Exceções
#
# Os erros geralmente são problemas de sintaxe, quando o código é digitado de forma errada.
#
# As exceções são "erros" que podem ocorrer por semântica ou problema de cálculos (por exemplo, divisão por zero).
#
# Algumas exceções:
# - NameError
# - ValueError
# - ZeroDivisionError
# - TypeError com Strings ou Inteiros
# - IndexError em Listas
# - KeyError em Dicionários

# Estruturas de Tratamento
#
# try:
#     OPERAÇÃO
# except:
#     FALHOU
# except TypeError:
#     FALHOU
# except ValueError:
#     FALHOU
# except OSError:
#     FALHOU
# else:                     #Opcional
#     DEU CERTO
# finally:                  #Opcional
#     FALHOU ou DEUCERTO

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except:
#     print('Infelizmente tivemos um problema :(')
# except Exception as erro:
#     print(f'O problema encontrado foi {erro.__class__}') #Informa a classe do erro (exceção) que aconteceu.
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
