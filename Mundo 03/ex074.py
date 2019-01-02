#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios
#e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e
#também indique o menor e o maior valor que estão na tupla.
print('\033[1;31m--=DESAFIO 74=--\033[1m')
from random import randint
tupla = randint(0,99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99)
print(tupla)
print(f'O maior número é {sorted(tupla)[4]} e o menor {sorted(tupla)[0]}.')
#Poderia usar max.(tupla)
