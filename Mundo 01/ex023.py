#Exercício Python 023: Faça um programa que leia um
#número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
print('\033[4;32m--=DESAFIO 23=--\033[m')
n = int(input('Digite um número de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('{} possui:'.format(n))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
