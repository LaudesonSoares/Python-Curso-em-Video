#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
#quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura=float(input('Qual a largura da parede? '))
altura=float(input('Qual a altura da parede? '))
area=largura*altura
tinta=area/2

print('A área da parede é {:.2f} M² e serão necessários {:.2f} litros de tinta para pinta-la.'.format(area,tinta))
