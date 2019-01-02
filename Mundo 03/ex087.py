#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
print('\033[1;31m--=DESAFIO 87=--\033[1m')
matriz = [[], [], [], []]
s1 = s2 = 0
for l in range(0,3):
    for c in range(0,3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        if n % 2 == 0:
            matriz[3].append(n)
        matriz[l].append(n)
print('\033[1;34m=' * 21)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('\033[1;34m=' * 21)
for par in matriz[3]:
    s1 += par
s2 = matriz[0][2] + matriz[1][2] + matriz[2][2]
maiorvalor = matriz[1][0]
if matriz[1][1] > matriz[1][2] and matriz[1][1] > matriz[1][0]:
    maiorvalor = matriz[1][1]
elif matriz[1][2] > matriz[1][1] and matriz[1][2] > matriz[1][0]:
    maiorvalor = matriz[1][2]
print(f'\033[1;30mA soma de todos os valores pares é {s1}.')
print(f'A soma dos valores da terceira coluna é {s2}.')
print(f'O maior valor da segunda linha é {maiorvalor}.')
