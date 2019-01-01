#Exercício Python 070: Crie um programa que leia o nome e o preço de vários
#produtos. O programa deverá perguntar se o usuário vai continuar ou não.
#No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
print('\033[1;31m--=DESAFIO 70=--')
print('\033[1;30m=' * 19)
print('\033[1;36mMERCADO DO NEGO BAM')
print('\033[1;30m=' * 19)
nome = continuar = preço = nomebarato = contador = total = mil = 0
while True:
    contador += 1
    nome = str(input('\033[1;33mNome do produto: ')).strip().title()
    preço = float(input('Valor do produto: \033[1;32mR$'))
    continuar = str(input('\033[1;36mDeseja incluir outro produto? [S/N]: ')).strip().upper()
    total += preço
    if contador == 1 or preço < valorbarato:
        valorbarato = preço
        nomebarato = nome
    if preço > 999:
        mil += 1
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('\033[1;31mÚltimo dado inválido! \033[1;36mDeseja incluir outro produto? [S/N]: ')).strip().upper()
    if continuar == 'S':
        print('\033[1;30m=' * 19)
    if continuar == 'N':
        break
print(f'\033[1;30mTotal gasto: R${total:.2f}.')
print(f'Produto mais barato: {nomebarato}')
if mil >= 1:
    print(f'Produtos que custam mais de R$1000.00: {mil}')
