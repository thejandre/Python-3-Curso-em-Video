#Exercício Python 066: Crie um programa que leia números inteiros
#pelo teclado. O programa só vai parar quando o usuário digitar
#o valor 999, que é a condição de parada. No final, mostre quantos
#números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
print('\033[1;31m--=DESAFIO 66=--')
contador = número = soma = 0
while True:
    número = int(input(f'\033[1;33mDigite o {contador + 1}º número: '))
    if número == 999:
        break
    contador += 1
    soma += número
if contador == 1:
    print(f'\033[1;30mVocê só digitou 1 número.\nOBS: Desconsiderando o flag.')
else:
    print(f'\033[1;30mVocê digitou {contador} números e a soma deles é {soma}.\nOBS: Desconsiderando o flag.')
