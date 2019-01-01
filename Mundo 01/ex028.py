#Exercício Python 028: Escreva um programa que faça o computador
#"pensar" em um número inteiro entre 0 e 5 e peça para o usuário
#tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import choice
from time import sleep
from termcolor import colored
print(colored('--=DESAFIO 28=--','red'))
lista = [0,1,2,3,4,5]
sorteado = choice(lista)
print('\033[1;33;m-=-\033[m' *20)
print('\033[1mA loteria acumulou! Participe escolhendo um número de 0 a 5.')
print('\033[1;33;m-=-\033[m' *20)
sleep(2.5)
numero = int(input('\033[1mDigite seu número: '))
if numero not in lista:
    print(colored('Inválido! O número apostado deve ser de 0 a 5.', 'red'))
    print('Aguarde, você tem mais uma chance.')
    sleep(2.5)
    numero = int(input('\033[1mÚltima chance! Digite um número de 0 a 5: '))
    if numero not in lista:
        print(colored('Inválido! Você perdeu.', 'red'))
    if numero in lista:
        if numero == sorteado:
            print(colored('Averiguando resultado...', 'blue'))
            sleep(2.5)
            print(colored('Que sorte! O número sorteado foi {}! Você venceu.'.format(sorteado), 'green'))
        if numero != sorteado:
            print(colored('Averiguando resultado...', 'blue'))
            sleep(2.5)
            print(colored('Que pena! O número sorteado foi {}. Você perdeu :('.format(sorteado), 'red'))
elif numero == sorteado:
    print(colored('Averiguando resultado...', 'blue'))
    sleep(2.5)
    print(colored('Que sorte! O número sorteado foi {}! Você venceu!'.format(sorteado), 'green'))
else:
    print(colored('Averiguando resultado...', 'blue'))
    sleep(2.5)
    print(colored('Que pena! O número sorteado foi {}. Você perdeu :('.format(sorteado), 'red'))
