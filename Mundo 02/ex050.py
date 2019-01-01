#Exercício Python 050: Desenvolva um programa que leia seis números
#inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.
print('\033[1;32m--=DESAFIO 50=--\033[m')
s = 0
for c in range(1,7):
    número = int(input('Digite o {}º número: '.format(c)))
    if número % 2 == 0:
        s += número
print('A soma desses números, desconsiderando os ímpares é: {}.'.format(s))
