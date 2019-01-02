#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de
#produtos e seus respectivos preços, na sequência. No final, mostre uma
#listagem de preços, organizando os dados em forma tabular.
print('\033[1;31m--=DESAFIO 76=--\033[1m')
print('\033[1;30m-\033[1m' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('\033[1;30m-' * 40)
listagem = ('Mansão', 1570000, 'Ferrari Black', 2974000, 'Dunhill Icon',
            1000, 'iPhone X', 4999, 'MacBook', 4999, 'Computador GTX 1080 TI x 3', 19000)
for c in range(len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<28}\033[1;32m{"R$"}\033[1;30m', end='')
    else:
        print(f'{listagem[c]:>10.2f}')
