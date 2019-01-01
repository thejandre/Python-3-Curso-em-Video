#Exercício Python 048: Faça um programa que calcule a
#soma entre todos os números que são múltiplos de
#três e que se encontram no intervalo de 1 até 500.
print('\033[1;31m--=DESAFIO 48=--\033[m')
s = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
print('O somatório dos números ímpares múltiplos de 3 de 1 a 500 é {}.'.format(s))
