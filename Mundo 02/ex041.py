#Exercício Python 041: A Confederação Nacional de Natação precisa de
#um programa que leia o ano de nascimento de um atleta e mostre
#sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date
print('\033[1;31m--=DESAFIO 41=--\033[m')
print('Vamos ver qual sua categoria na natação.')
nascimento = int(input('Digite seu nascimento: '))
ano = date.today().year
idade = ano - nascimento
if idade <= 9:
    print('Você tem {} anos e sua categoria é mirim.'.format(idade))
elif idade >= 10 and idade <= 14:
    print('Você tem {} anos e sua categoria é infantil.'.format(idade))
elif idade >=15 and idade <= 19:
    print('Você tem {} anos e sua categoria é junior.'.format(idade))
elif idade == 20:
    print('Você tem {} anos e sua categoria é sênior.'.format(idade))
else:
    print('Você tem {} anos e sua categoria é master.'.format(idade))
