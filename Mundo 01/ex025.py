#Exercício Python 025: Crie um programa que leia o
#nome de uma pessoa e diga se ela tem "SILVA" no nome.
print('\033[7;34;40m--=DESAFIO 25=--\033[m')
nome = str(input('Digite seu nome completo: ')).strip()
print('Você possui "SILVA" no nome: {}'.format('SILVA' in nome.upper().split()))
