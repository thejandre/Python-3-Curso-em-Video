#Exercício Python 072: Crie um programa que tenha uma dupla totalmente
#preenchida com uma contagem por extenso, de zero até vinte. Seu programa
#deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
print('\033[1;31m--=DESAFIO 72=--\033[1m')
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    continuar = 'Roacutan'
    número = int(input('Digite um número entre 0 e 20: '))
    if número < 0 or número > 20:
        número = int(input('\033[1;31mInválido! \033[1mDigite um número entre 0 e 20: '))
    if 0 <= número <= 20:
        print(f'Você digitou o número {extenso[número]}.')
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('\033[1;33mDeseja continuar? [S/N]: \033[1m')).strip().upper()
        if continuar == 'N':
            break
