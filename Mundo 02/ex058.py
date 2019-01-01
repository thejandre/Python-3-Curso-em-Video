#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador
#vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
#tentar adivinhar até acertar, mostrando no final quantos palpites
#foram necessários para vencer.
from random import randint
print('\033[1;31m--=DESAFIO 58=--')
print('\033[1;30mChutando de 0 à 10, tente adivinhar o número que o computador pensou.')
jogador = -1
computador = randint(0, 10)
tentativas = 1
while jogador != computador:
    jogador = int(input('\033[1;33m{}ª tentativa: '.format(tentativas)))
    tentativas += 1
if tentativas - 1 == 1:
    print('\033[1;30mIncrível! Você acertou de primeira.')
else:
    print('\033[1;30mVocê levou {} tentativas para adivinhar o número do computador.'.format(tentativas - 1))
