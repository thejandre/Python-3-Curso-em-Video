#Exercício Python 016: Crie um programa que leia um número
#Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
print('\033[1;30m--=DESAFIO 16=--\033[m')
from math import trunc
n = float(input('Digite um número real: '))
print('Sua parte inteira é {}'.format(trunc(n)))
