#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e
#carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também
#o ano de contratação e o salário. Calcule e acrescente, além da idade,
#com quantos anos a pessoa vai se aposentar.
from datetime import date
print('\033[1;31m--=DESAFIO 92=--\033[1m')
print('\033[1;34m=' * 31)
print(f'\033[1m{"SITUAÇÃO TRABALHISTA":-^31}')
print('\033[1;34m=' * 31)
pessoa = dict()
pessoa['nome'] = str(input('\033[1mNome: '))
pessoa['idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['carteira'] = int(input('Nº Carteira de trabalho [0 para não tem]: '))
if pessoa['carteira'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
print('\033[1;34m=' * 31)
print(f'\033[1mNome: {pessoa["nome"]}')
print(f'Idade: {pessoa["idade"]}')
print(f'CTPS: {pessoa["carteira"]}')
if pessoa['carteira'] != 0:
    print(f'\033[1mAno de contratação: {pessoa["contratação"]}')
    print(f'Salário: R${pessoa["salário"]:.2f}')
    contribuição = 35 - (date.today().year - pessoa["contratação"])
    if contribuição < 0:
        print(f'Aposentou-se com {pessoa["idade"] + contribuição} anos.')
    elif contribuição == 0:
        print(f'Vai se aposentar neste ano de {date.today().year}')
    else:
        print(f'Vai se aposentar com {pessoa["idade"] + contribuição} anos.')
    print(f'\033[1;34m{"FIM DO PROGRAMA":=^31}')
