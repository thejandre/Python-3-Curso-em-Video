#Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
#um de cada vez, para cada valor digitado pelo usuário. O programa será
#interrompido quando o número solicitado for negativo.
print('\033[1;31m--=DESAFIO 67=--')
while True:
    número = int(input('\033[1;33mDigite um número para ver sua tabuada, um número negativo encerra o programa: '))
    if número < 0:
        break
    for c in range(1, 11):
        print(f'\033[1;30m{número} x {c} = {número * c}')
