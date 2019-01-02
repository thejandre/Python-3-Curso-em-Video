#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

print('\033[1;31m--=DESAFIO 73=--\033[1m')
tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
          'Atlético', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
          'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC',
          'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print(f'Os últimos 4 colocados são (começando pelo último): {tabela[20:15:-1]}')
print(f'Tabela em ordem alfabética: {sorted(tabela)}')
print(f'O Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição.')
