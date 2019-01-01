#Exercício Python 060: Faça um programa que leia
#um número qualquer e mostre o seu fatorial.
print('\033[1;31m--=DESAFIO 60=--')
#USANDO FOR
número = int(input('\033[1;33mDigite um número e vamos descobrir o fatorial: '))
for c in range(número, 1, -1):
    número = número * (c - 1)
print('\033[1;30mSeu fatorial é', número)
#USANDO WHILE
n = int(input('\033[1;33mDigite um número para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end=(''))
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
