#Exercício Python 039: Faça um programa que leia o ano de nascimento
#de um jovem e informe, de acordo com a sua idade, se ele ainda vai
#se alistar ao serviço militar, se é a hora exata de se alistar ou
#se já passou do tempo do alistamento. Seu programa também deverá
#mostrar o tempo que falta ou que passou do prazo.
print('\033[1;31m--=DESAFIO 39=--\033[m')
from datetime import date
ano = date.today().year
nascimento = int(input('Digite em que ano você nasceu: '))
alistar = ano - nascimento
if alistar == 18:
    print('Você tem {} anos e está na hora de se alistar no serviço militar obrigatório!'.format(alistar))
elif alistar < 18:
    if alistar == 17:
        print('Você tem {} anos e falta 1 ano para que você precise se alistar no serviço militar obrigatório.'.format(alistar))
    elif alistar < 17:
        print('Você tem {} anos e faltam {} anos para que você precise se alistar no serviço militar obrigatório.'.format(alistar, 18 - alistar))
elif alistar == 19:
    print('Você tem {} anos e deveria ter se alistado no ano passado, espero que o tenha feito.'.format(alistar))
else:
    print('Você tem {} anos e deveria ter se alistado a {} anos atrás, espero que tenha o feito.'.format(alistar, alistar-18))
