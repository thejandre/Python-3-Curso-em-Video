#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.
print('\033[1;31m--=DESAFIO 55=--')
maiorpeso = 0
menorpeso = 0
for c in range(0, 5):
    peso = float(input('\033[1;33mPeso {}: '.format(1+c)))
    if c == 0:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('\033[1;30mO maior peso foi {:.1f}kgs e o menor peso foi {:.1f}kgs.'.format(maiorpeso, menorpeso))
