#Exercício Python 017: Faça um programa que leia o comprimento
#do cateto oposto e do cateto adjacente de um triângulo
#retângulo. Calcule e mostre o comprimento da hipotenusa.
print('\033[1;31m--=DESAFIO 17=--\033[m')
from math import sqrt
b = float(input('Cateto maior: '))
c = float(input('Cateto menor: '))
a = b**2 + c**2
print('A hipotenusa é {:.2f}!'.format(sqrt(a)))
