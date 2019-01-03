'''     Exercício Python 093: Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida. No final, tudo isso será guardado em um dicionário, incluindo o
total de gols feitos durante o campeonato.      '''

print('\033[1;31m--=DESAFIO 93=--\033[1m')
s = 0
jogador = {'nome': 'Nome', 'partidas': 0, 'gols': []}
print('\033[1;34m=' * 31)
jogador['nome'] = str(input('\033[1mNome do jogador: '))
print('\033[1;34m=' * 31)
jogador['partidas'] = int(input(f'\033[1mQuantas partidas {jogador["nome"]} jogou? '))
print('\033[1;34m=' * 31)
for c in range(jogador['partidas']):
    jogador['gols'].append(int(input(f'\033[1mQuantos gols na {c + 1}ª partida? ')))
print('\033[1;34m=' * 31)
for k, v in enumerate(jogador['gols']):
    s += v #poderia somar usando sum(jogador['gols'])
    print(f'\033[1;31m➡\033[1m Na partida {k + 1} marcou {v} gols.')
print(f'{"Total de {} gols.":^31}'.format(s))
print(f'\033[1;34m{"FIM DO PROGRAMA":=^31}')
