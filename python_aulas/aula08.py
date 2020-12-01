import random
num=random.random()
print(num)

import random
num = random.randint(0,10)
print(num)

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num,math.ceil(raiz)))

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num,math.floor(raiz)))

from math import sqrt,floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num,floor(raiz)))
