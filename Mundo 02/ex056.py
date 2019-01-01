#Exercício Python 056: Desenvolva um programa que leia o nome,
#idade e sexo de 4 pessoas. No final do programa, mostre:
#a média de idade do grupo, qual é o nome do homem mais
#velho e quantas mulheres têm menos de 20 anos.
print('\033[1;31m--=DESAFIO 56=--')
média = 0
velhoidade = 0
mulheridade = 0
for c in range(0, 4):
    print('\033[1;30m=== {}ª PESSOA ==='.format(c+1))
    nome = input('\033[1;33mNome: ').strip().title()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').lower().strip()
    if idade > 0:
        média += idade
    if idade > velhoidade and sexo == 'm':
        velhoidade = idade
        velhonome = nome
    if idade < 20 and sexo == 'f':
        mulheridade += 1
print('\033[1;30mA média de idade destas pessoas é {}.'.format(média / 4))
if velhoidade != 0:
    print('O homem mais velho é o {} com {} anos.'.format(velhonome, velhoidade))
if mulheridade == 1:
    print('Somente uma mulher tem menos de 20 anos.'.format(mulheridade))
elif mulheridade > 1:
    print('{} mulheres são menores de 20 anos.'.format(mulheridade))
