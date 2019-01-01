#Exercício Python 059: Crie um programa que leia
#dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.


from time import sleep
repetir = 1
print('\033[1;31m--=DESAFIO 59=--')
while repetir == 1:
    print('\033[1;30m=' * 59)
    print('Digite dois valores para posteriormente definir a operação.')
    print('=' * 59)
    contador = 0
    while contador != 2:
        contador += 1
        valor2 = int(input('\033[1;33m{}º valor: '.format(contador)))
        if contador == 1:
            valor1 = valor2
        if contador == 2:
            repetir = 3
            while repetir == 3:
                operação = 0
                print('\033[1;30m=' * 18)
                print('MENU DE OPERAÇÕES')
                print('=' * 18)
                print('[1] SOMAR')
                print('[2] MULTIPLICAR')
                print('[3] MAIOR')
                print('[4] ESCOLHER NOVAMENTE')
                print('[5] SAIR DO PROGRAMA')
                print('=' * 18)
                while operação < 1 or operação > 5:
                    operação = int(input('\033[1;33mOperação desejada: '))
                    if operação == 1:
                        print('\033[1;31mA soma dos números {} e {} é {}.'.format(valor1, valor2, valor1 + valor2))
                    elif operação == 2:
                        print('\033[1;31m{} multiplicado por {} é {}.'.format(valor1, valor2, valor1 * valor2))
                    elif operação == 3:
                        if valor1 > valor2:
                            print('\033[1;31mO valor {} é o maior digitado.'.format(valor1))
                        elif valor2 > valor1:
                            print('\033[1;31mO valor {} é o maior digitado.'.format(valor2))
                        else:
                            print('\033[1;31mOs dois valores são iguais.')
                    elif operação == 4:
                        repetir = 1
                    elif operação == 5:
                        print('\033[1;31mFinalizando...')
                        sleep(1.5)
                        repetir = 0
