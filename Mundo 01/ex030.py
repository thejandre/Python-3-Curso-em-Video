#Exercício Python 030: Crie um programa que leia um
#número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('\033[1;35m--=DESAFIO 30=--\033[m')
numero = int(input('Digite um número: '))
if numero % 2 == 1:
    print('O número {} é ÍMPAR.'.format(numero))
else:
    print('O número {} é PAR.'.format(numero))
