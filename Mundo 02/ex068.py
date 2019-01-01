#Exercício Python 068: Faça um programa que jogue par ou ímpar com o
#computador. O jogo só será interrompido quando o jogador perder, mostrando
#o total de vitórias consecutivas que ele conquistou no final do jogo.
from time import sleep
from random import choice
from random import randint
print('\033[1;31m--=DESAFIO 68=--')
quemcomeça = ['VOCÊ!', 'O COMPUTADOR!']
print('\033[1;36m=' * 50)
print('\033[1;30mVocê consegue vencer o computador no par ou ímpar?')
print('\033[1;36m=' * 50)
vconsecutivas = 0
pcescolha = ['par', 'ímpar']
while True:
    print('\033[1;30mE o direito de primeira escolha vai para...\033[1;31m')
    print('\033[1;36m=' * 50)
    sleep(3)
    começará = choice(quemcomeça)
    númeropc = randint(0, 10)
    print(f'\033[1;31m{começará}')
    if começará == 'VOCÊ!':
        escolha = str(input('\033[1;33mPar ou Ímpar? [P/I] ')).upper().strip()
        while escolha not in 'PI':
            escolha = str(input('\033[1;31mEscolha inválida! \033[1;33mPar ou Ímpar? [P/I] ')).upper().strip()
        númerojog = int(input('Digite seu número: '))
        resultado = númerojog + númeropc
        if resultado % 2 == 0:
            print(f'\033[1;30mVocê escolheu {númerojog} e o computador {númeropc}. {resultado} é par.')
        else:
            print(f'\033[1;30mVocê escolheu {númerojog} e o computador {númeropc}. {resultado} é ímpar.')
        if escolha == 'P':
            if resultado % 2 == 0:
                vconsecutivas += 1
                print('\033[1;32mIncrível! Você venceu!')
            else:
                print('\033[1;31mQue pena, você perdeu :(')
                if vconsecutivas == 0:
                    print('\033[1;30mVocê não venceu nenhuma vez :/')
                elif vconsecutivas == 1:
                    print('\033[1;30mVocê venceu uma vez.')
                else:
                    print(f'\033[1;30mVocê foi capaz de alcançar {vconsecutivas} vitórias consecutivas :O')
                break
        if escolha == 'I':
            if resultado % 2 != 0:
                vconsecutivas += 1
                print('\033[1;32mIncrível! Você venceu!')
            else:
                print('\033[1;31mQue pena, você perdeu :(')
                if vconsecutivas == 0:
                    print('\033[1;30mVocê não venceu nenhuma vez :/')
                elif vconsecutivas == 1:
                    print('\033[1;30mVocê venceu uma vez.')
                else:
                    print(f'\033[1;30mVocê foi capaz de alcançar {vconsecutivas} vitórias consecutivas :O')
                break
    else:
        escolhapc = choice(pcescolha)
        print(f'\033[1;30mO computador escolheu {escolhapc}.')
        númerojog = int(input('\033[1;33mDigite seu número: '))
        resultado = númerojog + númeropc
        if resultado % 2 == 0:
            print(f'\033[1;30mVocê escolheu {númerojog} e o computador {númeropc}. {resultado} é par.')
        elif resultado % 2 != 0:
            print(f'\033[1;30mVocê escolheu {númerojog} e o computador {númeropc}. {resultado} é ímpar.')
        if escolhapc == 'par':
            if resultado % 2 == 0:
                print('\033[1;31mQue pena, você perdeu :(')
                if vconsecutivas == 0:
                    print('\033[1;30mVocê não venceu nenhuma vez :/')
                elif vconsecutivas == 1:
                    print('\033[1;30mVocê venceu uma vez.')
                else:
                    print(f'\033[1;30mVocê foi capaz de alcançar {vconsecutivas} vitórias consecutivas :O')
                break
            else:
                vconsecutivas += 1
                print('\033[1;32mIncrível! Você venceu!')
        if escolhapc == 'ímpar':
            if resultado % 2 != 0:
                print('\033[1;31mQue pena, você perdeu :(')
                if vconsecutivas == 0:
                    print('\033[1;30mVocê não venceu nenhuma vez :/')
                elif vconsecutivas == 1:
                    print('\033[1;30mVocê venceu uma vez.')
                else:
                    print(f'\033[1;30mVocê foi capaz de alcançar {vconsecutivas} vitórias consecutivas :O')
                break
            else:
                vconsecutivas += 1
                print('\033[1;32mIncrível! Você venceu!')
