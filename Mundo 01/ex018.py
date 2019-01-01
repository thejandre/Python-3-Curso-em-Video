#Exercício Python 018: Faça um programa que leia um ângulo qualquer
#e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
print('\033[1;34m--=DESAFIO 18=--\033[m')
angulo = float(input('Digite o ângulo que deseja dissecar: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('Sendo o ângulo {}, seu seno é {:.2f}, seu cosseno é {:.2f} e seu tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))
