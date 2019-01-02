#Exercício Python 080: Crie um programa onde o usuário possa digitar
#cinco valores numéricos e cadastre-os em uma lista, já na posição correta
#de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
print('\033[1;31m--=DESAFIO 80=--\033[1m')
números = list()
for c in range(5):
    valor = int(input(f'Digite o {c + 1}º valor: '))
    if c == 0 or valor >= max(números):
        números.append(valor)
        print(f'Adicionado na posição {números.index(valor)} da lista.')
    else:
        posição = 0
        while True:
            if valor <= números[posição]:
                números.insert(posição, valor)
                print(f'Adicionado na posição {posição} da lista.')
                break
            posição += 1
print(f'Os valores foram, em ordem crescente: {números}')
