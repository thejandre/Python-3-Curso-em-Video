#Exercício Python 033: Faça um programa que leia
#três números e mostre qual é o maior e qual é o menor.
print('\033[1;31m--=DESAFIO 33=--\033[m')
print('\033[4;30mVamos descobrir qual é o menor e o maior número.\033[m')
#Números:
n1 = int(input('\033[33mDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: \033[1;32m'))
if n1 > n2 and n1 > n3:
    print(n1, 'é o maior número.')
if n2 > n1 and n2 > n3:
    print(n2, 'é o maior número.')
if n3 > n1 and n3 > n2:
    print(n3, 'é o maior número.')
if n1 < n2 and n1 < n3:
    print(n1, 'é o menor número.')
if n2 < n1 and n2 < n3:
    print(n2, 'é o menor número.')
if n3 < n1 and n3 < n2:
    print(n3, 'é o menor número.')
if n1 == n2 and n1 == n3:
    print('Os três números são iguais.')
if n1 == n2 and n1 != n3:
    print('Os números {} e {} são iguais.'.format(n1, n2))
if n1 == n3 and n1 != n2:
    print('Os números {} e {} são iguais.'.format(n1, n3))
if n2 == n3 and n2 != n1:
    print('Os números {} e {} são iguais.'.format(n2, n3))
