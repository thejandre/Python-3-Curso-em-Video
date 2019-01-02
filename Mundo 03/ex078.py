#Exercício Python 078: Faça um programa que leia 5 valores numéricos e
#guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor
#digitado e as suas respectivas posições na lista.
print('\033[1;31m--=DESAFIO 78=--\033[1m')
números = list()
for c in range(5):
    números.append(int(input(f'Digite o {c + 1}º número: ')))
print(f'Valores: {números}')
print(f'O maior valor digitado foi {max(números)} e ele está nas posições: ', end='')
for pos, num in enumerate(números):
    if num == max(números):
        print(f'{pos + 1} ', end='')
print(f'\nO menor valor digitado foi {min(números)} e ele está nas posições: ', end='')
for pos, num in enumerate(números):
    if num == min(números):
        print(f'{pos + 1} ', end='')
