#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

d6=int(input('Digite um número: '))
db=d6*2
tr=d6*3
rq=d6**(1/2)
print("Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}".format(db, tr, rq))