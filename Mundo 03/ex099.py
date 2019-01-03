'''    Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar
todos os valores e dizer qual deles é o maior.    '''

from time import sleep
from random import sample
def maior(* valores):
    if len(valores) >= 1:
        print(f'Análise dos valores', end=' ')
        for k, v in enumerate(valores):
            sleep(0.5)
            print(f'{v}', end=' ')
            if k == 0:
                maior = v
            if v > maior:
                maior = v
        print()
        print(f'Foram informados {len(valores)} valores.')
        print(f'O maior valor encontrado foi {maior}.')
    else:
        print('Nenhum valor informado.')


def linha():
    print('\033[1;34m-' * 31, '\033[1m')


print('\033[1;31m--=DESAFIO 99=--\033[1m')
linha()
maior(1, 5, 7, 6, 2)
linha()
maior(1, 9, 2, 4)
linha()
maior(1, 5, 2, 0)
linha()
maior(12)
linha()
maior()
print(f'\033[1;34m{"FIM DO PROGRAMA":-^31}')
