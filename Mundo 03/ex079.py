#Exercício Python 079: Crie um programa onde o usuário possa digitar vários
#valores numéricos e cadastre-os em uma lista. Caso o número já exista lá
#dentro, ele não será adicionado. No final, serão exibidos todos os valores
#únicos digitados, em ordem crescente.
print('\033[1;31m--=DESAFIO 79=--\033[1m')
números = list()
contador = 0
print('=' * 35)
while True:
    contador += 1
    add = int(input(f'Digite o {contador}º número: '))
    if add not in números:
        números.append(add)
        print('\033[1;32mSucesso!\033[1m Valor adicionado.')
        print('=' * 35)
        continuar = input('Deseja continuar? [S/N]: ').upper().strip()
    else:
        print('\033[1;31mInválido!\033[1m Número já adicionado anteriormente.')
        print('=' * 35)
        continuar = input('Deseja continuar? [S/N]: ').upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = input('\033[1;31mInválido! \033[1mDeseja continuar? [S/N]: ').upper().strip()
    if continuar == 'N':
        break
    else:
        print('=' * 35)
print('=' * 35)
print(f'{"Você digitou os valores:":=^35}')
print(f'{sorted(números)}')
print('=' * 35)
print(f'{"FIM DO PROGRAMA":=^35}')
print('=' * 35)
