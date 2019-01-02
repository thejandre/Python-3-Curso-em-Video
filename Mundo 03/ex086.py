#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3
#e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela,
#com a formatação correta.
print('\033[1;31m--=DESAFIO 86=--\033[1m')
matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
