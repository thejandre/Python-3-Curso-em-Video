print('\033[1;31m--=DESAFIO 89=--\033[1m')
provisória = list()
alunos = list()
c: int = 0
y: int = 0
while True:
    c += 1
    print(f'\033[1;33m{"{}º ALUNO":-^21}'.format(c))
    provisória.append(str(input('\033[1mNome: ').strip().title()))
    provisória.append(float(input('Primeira nota: ')))
    provisória.append(float(input('Segunda nota: ')))
    alunos.append(provisória[:])
    provisória.clear()
    print('\033[1;33m-' * 20)
    continuar = input('\033[1mDeseja cadastrar outro aluno? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('\033[1;31mInválido!\033[1m Deseja cadastrar outro aluno? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
print('\033[1;33m-' * 20)
print('\033[1;31mNº  \033[1;32mNOME     \033[1;35m  MÉDIA')
print('\033[1;33m-' * 20)
for c in range(len(alunos)):
    print(f'\033[1;31m{c:<4}\033[1;32m{alunos[c][0]:<12}', end='')
    print(f'\033[1;35m{(alunos[c][1] + alunos[c][2]) / 2:>4.1f}')
print('\033[1;33m-' * 20)
while True:
    deseja = int(input(f'\033[1mDeseja ver a nota de qual aluno?'
                       f' [0 à {c} ou 999 para interromper]: '))
    while deseja < 0 or deseja > c:
        if deseja == 999:
            break
        deseja = int(input(f'\033[1;31mInválido!\033[1m Deseja ver a nota'
                       f' de qual aluno? [0 à {c} ou 999 para interromper]: '))
    if deseja == 999:
        break
    else:
        print('\033[1;33m-' * 20)
        print(f'\033[1mNotas de {alunos[deseja][0]} são '
              f'{alunos[deseja][1:]}')
        print('\033[1;33m-' * 20)
