'''    Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e
mostre a área do terreno.   '''


def área(a, b):
    print(f'A área do terreno {a}x{b} é de {a * b}m².')


print('\033[1;31m--=DESAFIO 96=--\033[1m')
largura = float(input('LARGURA [M]: '))
comprimento = float(input('COMPRIMENTO [M]: '))
área(largura, comprimento)
