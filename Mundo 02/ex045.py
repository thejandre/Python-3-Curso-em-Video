#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
#OBS: Código enorme pois ainda não tinha aprendido os laços de repetição.
from random import choice
from termcolor import colored
from time import sleep
print('\033[1;31m--=DESAFIO 45=--')
print('\033[1;33m-=-' * 12)
print('\033[1;30mTente me vencer numa md3 de Jokenpô!')
print('\033[1;33m-=-' * 12)
sleep(2)
jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
jogo = ['pedra','papel','tesoura']
computador = choice(jogo)
print('\033[1;33mJogando...\033[m')
sleep(2)
if computador == 'pedra' and jogador == 'tesoura':
    pc = 'venceu'
    print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
if computador == 'pedra' and jogador == 'papel':
    pc = 'perdeu'
    print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
if computador == 'papel' and jogador == 'pedra':
    pc = 'venceu'
    print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
if computador == 'papel' and jogador == 'tesoura':
    pc = 'perdeu'
    print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
if computador == 'tesoura' and jogador == 'papel':
    pc = 'venceu'
    print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
if computador == 'tesoura' and jogador == 'pedra':
    pc = 'perdeu'
    print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
if computador == jogador:
    print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
    print('\033[1;33mDesempate!')
    jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
    jogo = ['pedra', 'papel', 'tesoura']
    computador = choice(jogo)
    print('\033[1;33mJogando...\033[m')
    sleep(2)
    if computador == 'pedra' and jogador == 'tesoura':
        pc = 'venceu'
        print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
    if computador == 'pedra' and jogador == 'papel':
        pc = 'perdeu'
        print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
    if computador == 'papel' and jogador == 'pedra':
        pc = 'venceu'
        print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
    if computador == 'papel' and jogador == 'tesoura':
        pc = 'perdeu'
        print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
    if computador == 'tesoura' and jogador == 'papel':
        pc = 'venceu'
        print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
    if computador == 'tesoura' and jogador == 'pedra':
        pc = 'perdeu'
        print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
    if computador == jogador:
        print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
        print('\033[1;33mDesempate!')
        jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
        jogo = ['pedra', 'papel', 'tesoura']
        computador = choice(jogo)
        print('\033[1;33mJogando...\033[m')
        sleep(2)
        if computador == 'pedra' and jogador == 'tesoura':
            pc = 'venceu'
            print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
        if computador == 'pedra' and jogador == 'papel':
            pc = 'perdeu'
            print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
        if computador == 'papel' and jogador == 'pedra':
            pc = 'venceu'
            print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
        if computador == 'papel' and jogador == 'tesoura':
            pc = 'perdeu'
            print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
        if computador == 'tesoura' and jogador == 'papel':
            pc = 'venceu'
            print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
        if computador == 'tesoura' and jogador == 'pedra':
            pc = 'perdeu'
            print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
        if computador == jogador:
            print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
            print('\033[1;33mDesempate!')
            jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
            jogo = ['pedra', 'papel', 'tesoura']
            computador = choice(jogo)
            print('\033[1;33mJogando...\033[m')
            sleep(2)
            if computador == 'pedra' and jogador == 'tesoura':
                pc = 'venceu'
                print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
            if computador == 'pedra' and jogador == 'papel':
                pc = 'perdeu'
                print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
            if computador == 'papel' and jogador == 'pedra':
                pc = 'venceu'
                print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
            if computador == 'papel' and jogador == 'tesoura':
                pc = 'perdeu'
                print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
            if computador == 'tesoura' and jogador == 'papel':
                pc = 'venceu'
                print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
            if computador == 'tesoura' and jogador == 'pedra':
                pc = 'perdeu'
                print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
            if computador == jogador:
                print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
                print('\033[1;33mDesempate!')
                jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
                jogo = ['pedra', 'papel', 'tesoura']
                computador = choice(jogo)
                print('\033[1;33mJogando...\033[m')
                sleep(2)
                if computador == 'pedra' and jogador == 'tesoura':
                    pc = 'venceu'
                    print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
                if computador == 'pedra' and jogador == 'papel':
                    pc = 'perdeu'
                    print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
                if computador == 'papel' and jogador == 'pedra':
                    pc = 'venceu'
                    print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
                if computador == 'papel' and jogador == 'tesoura':
                    pc = 'perdeu'
                    print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
                if computador == 'tesoura' and jogador == 'papel':
                    pc = 'venceu'
                    print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
                if computador == 'tesoura' and jogador == 'pedra':
                    pc = 'perdeu'
                    print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
                if computador == jogador:
                    print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
if pc == 'venceu':
    comput = 1
    jog = 0
if pc == 'perdeu':
    comput = 0
    jog = 1
sleep(1)
print('\033[1;33mJogo 2:')
sleep(2)
jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
jogo = ['pedra','papel','tesoura']
computador = choice(jogo)
print('\033[1;33mJogando...\033[m')
sleep(2)
if computador == 'pedra' and jogador == 'tesoura':
    pc = 'venceu'
    print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
if computador == 'pedra' and jogador == 'papel':
    pc = 'perdeu'
    print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
if computador == 'papel' and jogador == 'pedra':
    pc = 'venceu'
    print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
if computador == 'papel' and jogador == 'tesoura':
    pc = 'perdeu'
    print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
if computador == 'tesoura' and jogador == 'papel':
    pc = 'venceu'
    print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
if computador == 'tesoura' and jogador == 'pedra':
    pc = 'perdeu'
    print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
if computador == jogador:
    print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
    print('\033[1;33mDesempate!')
    jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
    jogo = ['pedra', 'papel', 'tesoura']
    computador = choice(jogo)
    print('\033[1;33mJogando...\033[m')
    sleep(2)
    if computador == 'pedra' and jogador == 'tesoura':
        pc = 'venceu'
        print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
    if computador == 'pedra' and jogador == 'papel':
        pc = 'perdeu'
        print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
    if computador == 'papel' and jogador == 'pedra':
        pc = 'venceu'
        print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
    if computador == 'papel' and jogador == 'tesoura':
        pc = 'perdeu'
        print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
    if computador == 'tesoura' and jogador == 'papel':
        pc = 'venceu'
        print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
    if computador == 'tesoura' and jogador == 'pedra':
        pc = 'perdeu'
        print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
    if computador == jogador:
        print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
        print('\033[1;33mDesempate!')
        jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
        jogo = ['pedra', 'papel', 'tesoura']
        computador = choice(jogo)
        print('\033[1;33mJogando...\033[m')
        sleep(2)
        if computador == 'pedra' and jogador == 'tesoura':
            pc = 'venceu'
            print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
        if computador == 'pedra' and jogador == 'papel':
            pc = 'perdeu'
            print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
        if computador == 'papel' and jogador == 'pedra':
            pc = 'venceu'
            print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
        if computador == 'papel' and jogador == 'tesoura':
            pc = 'perdeu'
            print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
        if computador == 'tesoura' and jogador == 'papel':
            pc = 'venceu'
            print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
        if computador == 'tesoura' and jogador == 'pedra':
            pc = 'perdeu'
            print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
        if computador == jogador:
            print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
            print('\033[1;33mDesempate!')
            jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
            jogo = ['pedra', 'papel', 'tesoura']
            computador = choice(jogo)
            print('\033[1;33mJogando...\033[m')
            sleep(2)
            if computador == 'pedra' and jogador == 'tesoura':
                pc = 'venceu'
                print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
            if computador == 'pedra' and jogador == 'papel':
                pc = 'perdeu'
                print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
            if computador == 'papel' and jogador == 'pedra':
                pc = 'venceu'
                print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
            if computador == 'papel' and jogador == 'tesoura':
                pc = 'perdeu'
                print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
            if computador == 'tesoura' and jogador == 'papel':
                pc = 'venceu'
                print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
            if computador == 'tesoura' and jogador == 'pedra':
                pc = 'perdeu'
                print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
            if computador == jogador:
                print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
                print('\033[1;33mDesempate!')
                jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
                jogo = ['pedra', 'papel', 'tesoura']
                computador = choice(jogo)
                print('\033[1;33mJogando...\033[m')
                sleep(2)
                if computador == 'pedra' and jogador == 'tesoura':
                    pc = 'venceu'
                    print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
                if computador == 'pedra' and jogador == 'papel':
                    pc = 'perdeu'
                    print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
                if computador == 'papel' and jogador == 'pedra':
                    pc = 'venceu'
                    print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
                if computador == 'papel' and jogador == 'tesoura':
                    pc = 'perdeu'
                    print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
                if computador == 'tesoura' and jogador == 'papel':
                    pc = 'venceu'
                    print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
                if computador == 'tesoura' and jogador == 'pedra':
                    pc = 'perdeu'
                    print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
                if computador == jogador:
                    print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
if pc == 'venceu':
    comput = 1 + comput
    jog = jog
elif pc == 'perdeu':
    comput = comput
    jog = 1 + jog
if comput == 2:
    print('\033[1;31mVocê perdeu a md3. O resultado foi Compoutador {} x {} Jogador.'.format(comput, jog))
elif jog == 2:
    print('\033[1;32mVocê venceu a md3. O resultado foi Computador {} x {} Jogador.'.format(comput, jog))
elif comput != 2 and jog != 2:
    sleep(1)
    print('\033[1;33mJogo 3:')
    sleep(2)
    jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
    jogo = ['pedra', 'papel', 'tesoura']
    computador = choice(jogo)
    print('\033[1;33mJogando...\033[m')
    sleep(2)
    if computador == 'pedra' and jogador == 'tesoura':
        pc = 'venceu'
        print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
    if computador == 'pedra' and jogador == 'papel':
        pc = 'perdeu'
        print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
    if computador == 'papel' and jogador == 'pedra':
        pc = 'venceu'
        print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
    if computador == 'papel' and jogador == 'tesoura':
        pc = 'perdeu'
        print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
    if computador == 'tesoura' and jogador == 'papel':
        pc = 'venceu'
        print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
    if computador == 'tesoura' and jogador == 'pedra':
        pc = 'perdeu'
        print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
    if computador == jogador:
        print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
        print('\033[1;33mDesempate!')
        jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
        jogo = ['pedra', 'papel', 'tesoura']
        computador = choice(jogo)
        print('\033[1;33mJogando...\033[m')
        sleep(2)
        if computador == 'pedra' and jogador == 'tesoura':
            pc = 'venceu'
            print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
        if computador == 'pedra' and jogador == 'papel':
            pc = 'perdeu'
            print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
        if computador == 'papel' and jogador == 'pedra':
            pc = 'venceu'
            print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
        if computador == 'papel' and jogador == 'tesoura':
            pc = 'perdeu'
            print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
        if computador == 'tesoura' and jogador == 'papel':
            pc = 'venceu'
            print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
        if computador == 'tesoura' and jogador == 'pedra':
            pc = 'perdeu'
            print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
        if computador == jogador:
            print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
            print('\033[1;33mDesempate!')
            jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
            jogo = ['pedra', 'papel', 'tesoura']
            computador = choice(jogo)
            print('\033[1;33mJogando...\033[m')
            sleep(2)
            if computador == 'pedra' and jogador == 'tesoura':
                pc = 'venceu'
                print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
            if computador == 'pedra' and jogador == 'papel':
                pc = 'perdeu'
                print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
            if computador == 'papel' and jogador == 'pedra':
                pc = 'venceu'
                print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
            if computador == 'papel' and jogador == 'tesoura':
                pc = 'perdeu'
                print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
            if computador == 'tesoura' and jogador == 'papel':
                pc = 'venceu'
                print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
            if computador == 'tesoura' and jogador == 'pedra':
                pc = 'perdeu'
                print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
            if computador == jogador:
                print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
                print('\033[1;33mDesempate!')
                jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
                jogo = ['pedra', 'papel', 'tesoura']
                computador = choice(jogo)
                print('\033[1;33mJogando...\033[m')
                sleep(2)
                if computador == 'pedra' and jogador == 'tesoura':
                    pc = 'venceu'
                    print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
                if computador == 'pedra' and jogador == 'papel':
                    pc = 'perdeu'
                    print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
                if computador == 'papel' and jogador == 'pedra':
                    pc = 'venceu'
                    print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
                if computador == 'papel' and jogador == 'tesoura':
                    pc = 'perdeu'
                    print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
                if computador == 'tesoura' and jogador == 'papel':
                    pc = 'venceu'
                    print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
                if computador == 'tesoura' and jogador == 'pedra':
                    pc = 'perdeu'
                    print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
                if computador == jogador:
                    print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
                    print('\033[1;33mDesempate!')
                    jogador = str(input('\033[1;30mVocê escolhe pedra, papel ou tesoura? \033[m')).lower().strip()
                    jogo = ['pedra', 'papel', 'tesoura']
                    computador = choice(jogo)
                    print('\033[1;33mJogando...\033[m')
                    sleep(2)
                    if computador == 'pedra' and jogador == 'tesoura':
                        pc = 'venceu'
                        print('\033[1;31mVocê perdeu! Eu escolhi pedra, e pedra vence tesoura.')
                    if computador == 'pedra' and jogador == 'papel':
                        pc = 'perdeu'
                        print(colored('\033[1mVocê venceu! Eu escolhi pedra e papel vence pedra.', 'green'))
                    if computador == 'papel' and jogador == 'pedra':
                        pc = 'venceu'
                        print('\033[1;31mVocê perdeu! Eu escolhi papel, e papel vence pedra.')
                    if computador == 'papel' and jogador == 'tesoura':
                        pc = 'perdeu'
                        print(colored('\033[1mVocê venceu! Eu escolhi papel e tesoura vence papel.', 'green'))
                    if computador == 'tesoura' and jogador == 'papel':
                        pc = 'venceu'
                        print('\033[1;31mVocê perdeu! Eu escolhi tesoura, e tesoura vence papel.')
                    if computador == 'tesoura' and jogador == 'pedra':
                        pc = 'perdeu'
                        print(colored('\033[1mVocê venceu! Eu escolhi tesoura e pedra vence tesoura.', 'green'))
                    if computador == jogador:
                        print('\033[1;34mEmpate! Eu também escolhi {}.'.format(computador))
    if pc == 'venceu':
        comput = 1 + comput
        jog = jog
    elif pc == 'perdeu':
        comput = comput
        jog = 1 + jog
    if comput > jog:
        print('\033[1;31mVocê perdeu a md3. O resultado foi Compoutador {} x {} Jogador.'.format(comput, jog))
    elif jog > comput:
        print('\033[1;32mVocê venceu a md3. O resultado foi Computador {} x {} Jogador.'.format(comput, jog))
