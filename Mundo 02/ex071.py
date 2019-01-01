#Exercício Python 071: Crie um programa que simule o funcionamento
#de um caixa eletrônico. No início, pergunte ao usuário qual será
#o valor a ser sacado (número inteiro) e o programa vai informar
#quantas cédulas de cada valor serão entregues.
print('\033[1;31m--=DESAFIO 71=--')
print('\033[1;30m=' * 16)
print('Caixa Eletrônico')
print('=' * 16)
saque = céd50 = céd20 = céd10 = céd1 = 0
valor = int(input('\033[1;33mQuanto deseja sacar? \033[1;32mR$\033[1;30m'))
while 50 <= valor - saque:
    saque += 50
    céd50 += 1
while 20 <= valor - saque:
    saque += 20
    céd20 += 1
while 10 <= valor - saque:
    saque += 10
    céd10 += 1
while 1 <= valor - saque:
    saque += 1
    céd1 += 1
print('Você receberá:')
if céd50 == 1:
    print(f'{céd50} cédula de R$50.00')
if céd50 > 1:
    print(f'{céd50} cédulas de R$50.00')
if céd20 == 1:
    print(f'{céd20} cédula de R$20.00')
if céd20 > 1:
    print(f'{céd20} cédulas de R$20.00')
if céd10 == 1:
    print(f'{céd10} cédula de R$10.00')
if céd10 > 1:
    print(f'{céd10} cédulas de R$10.00')
if céd1 == 1:
    print(f'{céd1} moeda de R$1.00')
if céd1 > 1:
    print(f'{céd1} moedas de R$1.00')
