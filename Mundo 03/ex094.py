'''     Exercício Python 094: Crie um programa que leia nome, sexo e idade de
várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média    '''

print('\033[1;31m--=DESAFIO 94=--\033[1m')
grupo = dict()
lista = list()
print('\033[1;34m=' * 31)
c = s = 0
while True:
    grupo.clear()
    c += 1
    grupo['nome'] = str(input('\033[1mNome: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('\033[1;31mInválido! \033[1mSexo [M/F]: ')).upper().strip()
    grupo['sexo'] = sexo
    grupo['idade'] = int(input('Idade: '))
    s += grupo['idade']
    lista.append(grupo.copy())
    print('\033[1;34m=' * 31)
    continuar = str(input('\033[1mDeseja continuar? [S/N]: ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('\033[1;31mInválido! \033[1mDeseja continuar? [S/N]: ')).upper().strip()
    if continuar == 'N':
        break
    print('\033[1;34m=' * 31)
print('\033[1;34m=' * 31)
print(f'\033[1m{c} pessoas cadastradas.')
print(f'A média de idade do grupo é de {s / c:.2f}.')
print('[1;31mMulheres cadastradas:', end=' ')
for k, v in enumerate(lista):
    if lista[k]['sexo'] == 'F':
        print(f'{lista[k]["nome"]}', end=' ')
print()
print('As pessoas do grupo com idade acima da média são: ')
for cont in range(c):
    if lista[cont]['idade'] > s / c:
        print(f'{lista[cont]["nome"]}, {lista[cont]["sexo"]},'
              f' {lista[cont]["idade"]}')
print(f'\033[1;34m{"FIM DO PROGRAMA":=^31}')
