from random import randint
#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA
#a criar palpites.O programa vai perguntar quantos jogos serão gerados e
#vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em
#uma lista composta.
from time import sleep
from random import sample
print(f'\033[1;31m{"DESAFIO 88":-^33}\033[1m')
print(f'\033[1;34m{"=":=^33}')
print(f'\033[1;30m{"GERADOR MEGA DA VIRADA":-^33}')
print(f'\033[1;34m{"=":=^33}')
jogos = list()
quantidade = int(input('\033[1m\033[1;33mDigite a quantidade de jogos deseja gerar: '))
sleep(0.5)
print(f'\033[1;34m{"GERANDO APOSTAS":=^33}\033[1;30m')
sleep(1)
for c in range(quantidade):
    jogos.append(sample(range(1, 60), 6))
for a, j in enumerate(jogos):
    print(f'Jogo {a + 1}: {sorted(j)}')
    sleep(0.3)
print(f'\033[1;34m{"BOA SORTE":=^33}\033[1;30m')
