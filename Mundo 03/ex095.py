'''     Exercício Python 095: Aprimore o desafio 93 para que ele
funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.      '''

print('\033[1;31m--=DESAFIO 95=--\033[1m')
jogadores = list()
c = 0
while True:
    jogador = {'nome': 0, 'gols': [], 'totgols': 0}
    s = 0
    c += 1
    print(f'\033[1;34m{"JOGADOR {}":=^37}'.format(c))
    jogador['nome'] = str(input('\033[1mNome: ')).title()
    p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for cont in range(p):
        gol = int(input(f'Quantos gols na {cont + 1}ª partida? '))
        s += gol
        jogador['gols'].append(gol)
        del gol
    jogador['totgols'] = s
    jogadores.append(jogador.copy())
    jogador.clear()
    print('\033[1;34m=' * 37)
    while True:
        continuar = str(input('\033[1mDeseja continuar? [S/N]: ')).upper().strip()
        if continuar != 'S' and continuar != 'N':
            print('\033[1;31mInválido! \033[1mDigite apenas S para sim ou N para não.')
        else:
            break
    if continuar == 'N':
        break
print('\033[1;34m=' * 37)
for k, v in enumerate(jogadores[0]):
    print(f'\033[1;31m{v.title():<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'\033[1m{k:>1}    ', end='')
    for v in v.values():
        print(f'{str(v):<15}', end='')
    print()
print('\033[1;34m=' * 37)
while True:
    resp = int(input('\033[1mDeseja fazer o levantamento de qual jogador? [999 interrompe]: '))
    if resp != 999:
        if resp < 0 or resp > c - 1:
            print(f'\033[1;31mInválido!\033[1m Digite um código de 0 à {c - 1} ou 999 para parar.')
        else:
            print('\033[1;34m=' * 37)
            print(f'\033[1m{jogadores[resp]["nome"]:^37}')
            for cont in range(len(jogadores[resp]["gols"])):
                print(f'{"{}ª partida: {} gols.":^37}'.format(cont + 1, jogadores[resp]["gols"][cont]))
            print('\033[1;34m=' * 37)
    elif resp == 999:
        break
print(f'\033[1;34m{"FIM DO PROGRAMA":=^37}')
