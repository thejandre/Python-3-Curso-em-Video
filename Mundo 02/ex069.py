#Exercício Python 069: Crie um programa que leia a idade e o sexo
#de várias pessoas. A cada pessoa cadastrada, o programa deverá
#perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
print('\033[1;31m--=DESAFIO 69=--')
contador = maiordeidade = homens = mulhermenor = 0
while True:
    continuar = sexo = 0
    contador += 1
    print(f'\033[1;36m=-=-=-{contador}ª PESSOA-=-=-=')
    nome = str(input('\033[1;33mNome: ')).upper().strip()
    idade = int(input('Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if idade >= 18:
        maiordeidade += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulhermenor += 1
    if sexo == 'M' or sexo == 'F':
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('\033[1;35mDeseja cadastrar outra pessoa? [S/N]: ')).upper().strip()
    if continuar == 'N':
        break
if contador == 1:
    print('\033[1;30mUma pessoa cadastrada.')
else:
    print(f'\033[1;30m{contador} pessoas cadastradas.')
if maiordeidade > 1:
    print(f'\033[1;30m{maiordeidade} pessoas maiores de 18 anos cadastradas.')
elif maiordeidade == 0:
    print('Ninguém maior de idade cadastrado..')
elif maiordeidade == 1:
    print('Somente um maior de idade cadastrado.')
else:
    print('Nenhum maior de idade cadastrado.')
if homens == 0:
    print('Nenhum homem cadastrado.')
elif homens == 1:
    print('Um homem cadastrado.')
else:
    print(f'{homens} homens cadastrados.')
if mulhermenor == 0:
    print('Nenhuma mulher com menos de 20 anos cadastrada.')
if mulhermenor == 1:
    print('Uma mulher com menos de 20 anos cadastrada.')
if mulhermenor > 1:
    print(f'{mulhermenor} mulheres com menos de 20 anos cadastradas.')
