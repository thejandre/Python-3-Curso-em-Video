#Exercício Python 011: Faça um programa que leia a largura e a altura de
#uma parede em metros, calcule a sua área e a quantidade de tinta necessária
#para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
print('\033[1;34m--=DESAFIO 11=--\033[m')
print('É importante que você responda as perguntas a seguir usando a medida metro.')
a = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
area = a*l
q = area/2
print('A área desta parede é de {:.2f}m². Para pintá-la, será necessário {:.2f} litros de tinta.'.format(area, q))
