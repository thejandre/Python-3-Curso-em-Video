#Exercício Python 064: Crie um programa que leia vários números inteiros
#pelo teclado. O programa só vai parar quando o usuário digitar o valor
#999, que é a condição de parada. No final, mostre quantos números foram
#digitados e qual foi a soma entre eles (desconsiderando o flag).
print('\033[1;31m--=DESAFIO 64=--')
número = soma = 0
quantidade = -1
while número != 999:
     soma += número
     quantidade += 1
     número = int(input('\033[1;33mDigite qualquer número: (999 para parar) '))
print('\033[1;30mForam digitados {} números e a soma deles é {}. (Desconsiderando o 999)'.format(quantidade, soma))
