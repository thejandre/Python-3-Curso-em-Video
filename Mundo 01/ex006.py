#Exercício Python 006: Crie um algoritmo que leia um número e
#mostre o seu dobro, triplo e raiz quadrada.
print('\033[1;33m--=DESAFIO 6=--\033[m')
n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {} é {}.'.format (n, d))
print('O triplo de {} é {}.'.format (n, t))
print('A raiz quadrada de {} é {}.'.format (n, r))
