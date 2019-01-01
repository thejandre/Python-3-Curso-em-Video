#Exercício Python 035: Desenvolva um programa que leia o comprimento
#de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('\033[1;31m--=DESAFIO 35=--\033[m')
r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As 3 retas formam um triângulo.')
else:
    print('As três retas não podem formar um triângulo.')
