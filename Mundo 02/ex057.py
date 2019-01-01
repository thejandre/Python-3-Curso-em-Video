#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
#mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
#digitação novamente até ter um valor correto.
print('\033[1;31m--=DESAFIO 57=--\033[m')
sexo = 'Início'
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Sexo [M/F]: ')).upper()
print('Resposta: {}'.format(sexo))