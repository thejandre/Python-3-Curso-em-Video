#Exercício Python 081: Crie um programa que vai ler
#vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
print('\033[1;31m--=DESAFIO 81=--\033[1m')
números = list()
c = 0
print('=' * 55)
while True:
    c += 1
    números.append(int(input(f'Digite o {c}º valor: ')))
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('\033[1;31mInválido! \033[1mDeseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
números.sort(reverse=True)
print('=' * 55)
if c > 1:
    print(f'Foram digitados {c} números.')
else:
    print('Foi digitado 1 número.')
print(f'Os números digitados são, de forma decrescente: {números}')
if 5 in números:
    if números.count(5) > 1:
        print(f'O valor 5 foi digitado {números.count(5)} vezes.')
    else:
        print('O valor 5 foi digitado uma vez.')
else:
    print('O valor 5 não foi digitado.')
print(f'{"FIM DO PROGRAMA":=^55}')
