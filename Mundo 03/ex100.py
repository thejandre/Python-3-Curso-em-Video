'''    Exercício Python 100: Faça um programa que tenha uma lista chamada números e
duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
valores pares sorteados pela função anterior.    '''

from random import sample
from time import sleep
def sorteia():
    números.append(sample(range(0, 10), 5))
    print('Sorteando: ', end='')
    sleep(0.5)
    for v in números[0]:
        print(f'{v}', end=' ')
        sleep(0.5)
    print()


def somaPar():
    s = 0
    for v in números[0]:
        if v % 2 == 0:
            s += v
    print(f'A soma dos números pares entre os sorteados é {s}.')


print('\033[1;31m--=DESAFIO 90=--\033[1m')
números = list()
sorteia()
somaPar()
