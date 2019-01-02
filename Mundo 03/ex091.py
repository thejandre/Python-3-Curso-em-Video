'''     Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e
tenham resultados aleatórios. Guarde esses resultados em um dicionário em
Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado.   '''

print('\033[1;31m--=DESAFIO 91=--\033[1m')
from random import randint
from operator import itemgetter
from time import sleep
c = 0
jogadores = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
print(f'\033[1;34m{"SORTEANDO":=^31}')
sleep(0.6)
for j, r in jogadores.items():
    print(f'\033[1mO {j} sorteou {r}.')
    sleep(0.6)
print(f'\033[1;34m{"RANKING":=^31}')
for k, v in sorted(jogadores.items(), key=itemgetter(1), reverse=True):
    c += 1
    print(f'\033[1m{c}º lugar: {k} com {v}.')
    sleep(0.6)
print(f'\033[1;34m{"FIM DO PROGRAMA":=^31}')
