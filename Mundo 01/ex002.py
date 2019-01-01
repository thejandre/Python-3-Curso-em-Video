#Exercício Python 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
print('\033[1;31m--=DESAFIO 2=--\033[m')
nome = input('Qual é o seu nome? ')
#print('É um prazer conhecê-lo,', nome)
print('É um prazer conhecê-lo, \033[33m{}\033[m!' .format(nome))
