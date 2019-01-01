#Exercício Python 024: Crie um programa que leia o
#nome de uma cidade diga se ela começa ou não com o nome "SANTO".
print('\033[1;31m--=DESAFIO 24=--\033[m')
cidade = input('Digite o nome de uma cidade: ')
print('Está cidade se inicia com "SANTO":', cidade.lstrip().upper().startswith('SANTO '))
