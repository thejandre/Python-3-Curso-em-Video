'''    Exercício Python 098: Faça um programa que tenha uma função chamada
contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada   '''

from random import randint
from time import sleep
def contador(a, b, c):
    print(f'Contagem de {a} a {b} de {c} em {c}')
    if a < b:
        for c in range(a, b + 1, c):
            print(f'{c}', end=' -> ')
            sleep(0.3)
        print()
    if a > b:
        for c in range(a, b - 1, -c):
            print(f'{c}', end=' -> ')
            sleep(0.3)
        print()


def linha():
    print('\033[1;34m-' * 31, '\033[1m')


print('\033[1;31m--=DESAFIO 98=--\033[1m')
linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Contagem personalizada: você quem define os parâmetros!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo [0 = aleatório de 1 a 10]: '))
if passo == 0:
    passo = randint(1, 10)
elif passo < 0:
    passo = passo - passo - passo
linha()
contador(início, fim, passo)
