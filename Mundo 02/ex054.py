#Exercício Python 054: Crie um programa que leia o ano de nascimento de
#sete pessoas. No final, mostre quantas pessoas ainda não atingiram
#a maioridade e quantas já são maiores.
from datetime import date
print('\033[1;33m--=DESAFIO 54=--')
maioridade = 0
for c in range(0, 7):
    nascimento = int(input('Digite o ano em que esta pessoa nasceu: '))
    if date.today().year - nascimento >= 21:
        maioridade += 1
print('Destas 7 pessoas, {} já são maiores e {} não são.'.format(maioridade, 7 - maioridade))
