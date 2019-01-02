#Exercício Python 085: Crie um programa onde o usuário possa digitar sete
#valores numéricos e cadastre-os em uma lista única que mantenha separados
#os valores pares e ímpares. No final, mostre os valores pares e ímpares
#em ordem crescente.
print('\033[1;31m--=DESAFIO=--\033[1m')
números = [[], []]
for c in range(7):
    n = int(input(f'Digite o {c + 1}º número: '))
    if n % 2 == 0:
        números[0].append(n)
    else:
        números[1].append(n)
print(f'Pares: {sorted(números[0])}')
print(f'Ímpares: {sorted(números[1])}')
