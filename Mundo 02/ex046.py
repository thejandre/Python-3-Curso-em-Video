#Exercício Python 046: Faça um programa que mostre na tela uma contagem
#regressiva para o estouro de fogos de artifício, indo de 10 até 0, com
#uma pausa de 1 segundo entre eles.
print('\033[1;31m--=DESAFIO 46=--\033[m')
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FOGOS :P')
