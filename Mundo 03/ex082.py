#Exercício Python 082: Crie um programa que vai ler vários números e
#colocar em uma lista. Depois disso, crie duas listas extras que vão
#conter apenas os valores pares e os valores ímpares digitados,
#respectivamente. Ao final, mostre o conteúdo das três listas geradas.
print('\033[1;31m--=DESAFIO 82=--\033[1m')
par = list()
ímpar = list()
números = list()
c = 0
while True:
    print('=' * 40)
    c += 1
    números.append(int(input(f'Digite o {c}º número: ')))
    continuar = input('Deseja continuar? [S/N]: ').upper().strip()
    while continuar != 'S' and continuar != 'N':
        print('=' * 40)
        continuar = input('\033[1;31mInválido! \033[1mDeseja continuar? [S/N]: ').upper().strip()
    if continuar == 'N':
        print('=' * 40)
        break
for c in range(len(números)):
    if números[c] % 2 == 0:
        par.append(números[c])
    else:
        ímpar.append(números[c])
print(f'Lista total: {números}\nLista par: {par}')
print(f'Lista ímpar: {ímpar}')
print(f'{"FIM DO PROGRAMA":=^40}')