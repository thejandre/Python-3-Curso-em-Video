#Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.
print('\033[1;31m--=DESAFIO 3=--\033[m')
n1 = int(input('Primeiro número = '))
n2 = int(input('Segundo número = '))
s = n1+n2
#print('A soma entre', n1, 'e', n2, 'vale', s)
print('A soma entre {} e {} vale {}' .format(n1, n2, s))
