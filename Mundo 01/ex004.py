#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na
#tela o seu tipo primitivo e todas as informações possíveis sobre ele.
print('\033[1;31m--=DESAFIO 4=--\033[m')
a0 = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(a0))
print('É um número?', a0.isnumeric())
print('É alfabético?', a0.isalpha())
print('Está em maiúsculas?', a0.isupper())
print('É um espaço?', a0.isspace())
print('Está capitalizada?', a0.istitle())
print('Está em minúsculas?', a0.islower())
