#Exercício Python 032: Faça um programa que
#leia um ano qualquer e mostre se ele é bissexto.
print('\033[1;31m--=DESAFIO 32=--\033[m')
d1 = int(input('Digite um ano e veremos se ele é bissexto: '))
if d1 % 4 == 0 and d1 % 100 != 0:
    print('Este ano é bissexto! Fevereiro possui 29 dias.')
else:
    print('Este ano não é bissexto!')
