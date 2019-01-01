#Exercício Python 052: Faça um programa que leia um
#número inteiro e diga se ele é ou não um número primo.
print('\033[1;34m--=DESAFIO 52=--')
número = int(input('\033[1;33mDigite um número e vamos ver se ele é primo: '))
cont = 0
for c in range(1, número+1):
    if número % c == 0:
        cont += 1
if cont == 2:
    print('Este número é primo.')
else:
    print('Este número não é primo.')
