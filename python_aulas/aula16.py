# Tuplas
#
# Tuplas são estruturas de variáveis compostas onde múltiplas informações são guardadas em grupo na memória.
# Tuplas possuem as seguintes características
#
# São definidas por ()
# São imutáveis

# Criando uma tupla
# Nas versões mais recents do Python, não é necessário usar ()

lanche = ("Hamburger", "Batata", "Cenoura", "Banana")

print("Imprimindo uma tupla inteira")
print(lanche)
print()

print("Imprimindo o elemento 1 da tupla") # Lembrar que indices do python começam em 0
print(lanche[1])
print()

print("Imprimindo o penultimo elemento")
print(lanche[-2])
print()

print("Imprimindo  o intervalo fatiado [1:3]")
print(lanche[1:3])
print("Note que o elemento {}, índice 0, fica de fora. Enquanto o elemento {}, índice 3, "
      "também fica de fora pois o intervalo vai de 1 a 3, sem incluir 3.".format(lanche[0], lanche[3]))
print()

print("Imprimindo no antepenúltimo até o final")
print(lanche[-3:])
print()

# Lembre que tuplas são imutáveis. Remova o comentário da linha seguinte para verificar o erro.

# lanche[1] = "refrigerante"

# Loop for para tuplas

# (1) Loop for baseado na tupla
# Note que a sintaxe é mais simples
# Note que não te permite identificar a posição do elemento

print("Loop for com base na tupla")
for comida in lanche:
    print("Vou comer {}.".format(comida))
print("Granolei demais, estou com 97% de BF.")
print()

# Note que para o loop baseado em ranges, é possível identificar a posição do elemento.

print("Loop for com base em intervalos")
for cont in range(0, len(lanche)):
    print("Vou comer {}, salvo como elemento {}.".format(lanche[cont], cont))
print("Granolei demais, meu BF aumentou para 107%.")
print()

# Outra forma de fazer um loop identificando a posição do elemento é

for pos, comida in enumerate(lanche):
    print("Vou comer {}, salvo como elemento {}.".format(comida, pos))
print()

print("Impressão de tuplas ordenadas")
print(sorted(lanche))
print()

print("Soma de tuplas é basicamente uma soma de strings ou um concatenar")
a = (2, 4, 5)
b = (3, 5, 7, 9)
c = a + b
d = b + a
print("a + b = c = {}".format(c))
print("b + a = d = {}".format(d))
print("contagem de número 5 na tupla c é {}".format(c.count(5)))
print("o index do número 4 na tupla c é a posição {}".format(c.index(4)))

# max() e min() podem ser utilizados para encontrar o maior e menor valor em uma tuplas.