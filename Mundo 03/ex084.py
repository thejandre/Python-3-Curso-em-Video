#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
#guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
print(f'\033[1;31m{"DESAFIO 84":-^45}\033[1m')
pessoas = list()
provisória = list()
imc = list()
maiorpeso = list()
menorpeso = list()
maiorpesonome = list()
menorpesonome = list()
c = 0
print('\033[34;1m=' * 45)
print('\033[1;30m', f'{"CALCULADOR DE IMC DE GRUPO DE PESSOAS":^45}')
print('\033[1;34m=' * 45, '\033[1;30m')
print(f'{"Abaixo do peso":.<31}', end='')
print(f'{"Abaixo de 18.4":>14}')
print(f'{"Peso normal":.<31}', end='')
print(f'{"18.5 - 24.9":>14}')
print(f'{"Sobrepeso":.<31}', end='')
print(f'{"25.0 - 29.9":>14}')
print(f'{"Obesidade Grau I":.<31}', end='')
print(f'{"30.0 - 34.9":>14}')
print(f'{"Obesidade Grau II":.<31}', end='')
print(f'{"35.0 - 39.9":>14}')
print(f'{"Obesidade Grau III":.<31}', end='')
print(f'{"Acima de 40":>14}')
print('\033[34;1m=' * 45, '\033[1;30m')
while True:
    c += 1
    provisória.append(str(input(f'\033[1;30mDigite o nome da {c}ª pessoa: ')).title().strip())
    provisória.append(int(input(f'Digite a idade da {c}ª pessoa: ')))
    provisória.append(float(input(f'Digite o peso da {c}ª pessoa: ')))
    if c == 1 or provisória[2] > maiorpeso[0][2]:
        maiorpeso.clear()
        maiorpesonome.clear()
        maiorpeso.append(provisória[:])
        maiorpesonome.append(provisória[0])
        if c == 1:
            menorpeso.append(provisória[:])
            menorpesonome.append(provisória[0])
    elif c != 1 and provisória[2] == maiorpeso[0][2]:
        maiorpeso.append(provisória[:])
        maiorpesonome.append(provisória[0])
    elif provisória[2] > maiorpeso[0][2]:
        maiorpeso.clear()
        maiorpesonome.clear()
        maiorpeso.append(provisória[:])
        maiorpesonome.append(provisória[0])
    if c != 1 and provisória[2] == menorpeso[0][2]:
        menorpeso.append(provisória[:])
        menorpesonome.append(provisória[0])
    elif provisória[2] < menorpeso[0][2]:
        menorpeso.clear()
        menorpesonome.clear()
        menorpeso.append(provisória[:])
        menorpesonome.append(provisória[0])
    provisória.append(float(input(f'Digite a altura (em cm) da {c}ª pessoa: ')))
    pessoas.append(provisória[:])
    provisória.clear()
    print('\033[1;34m=' * 45, '\033[1;30m')
    continuar = input('Deseja continuar? [S/N]: \033[1;34m').upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = input('\033[1;31mInválido! \033[1;30mDeseja continuar? [S/N]: \033[1;34m').upper().strip()
    if continuar == 'N':
        break
    print('\033[1;34m=' * 45)
print('=' * 45)
print('\033[1;30m{} pessoas cadastradas.'.format(c))
print(f'Maior peso: {maiorpeso[0][2]}kg de {maiorpesonome}')
print(f'Menor peso: {menorpeso[0][2]}kg de {menorpesonome}\033[1;34m')
print(f'{"PESSOAS CADASTRADAS":=^45}')
for b in range(0, c):
    imc = pessoas[b][2] / ((pessoas[b][3] / 100) * (pessoas[b][3] / 100))
    print(f'\033[1;30mNome: {pessoas[b][0]}')
    print(f'Idade: {pessoas[b][1]}')
    print(f'IMC: {imc:.2f}', end=' » ')
    if imc <= 18.4:
        print('\033[1;30mAbaixo do peso ideal.\033[1;34m')
    elif 18.5 <= imc <= 24.9:
        print('\033[1;30mPeso ideal\033[1;34m')
    elif 25 <= imc <= 29.9:
        print('\033[1;30mSobrepeso\033[1;34m')
    elif 30 <= imc <= 34.9:
        print('\033[1;30mObesidade Grau I\033[1;34m')
    elif 35 <= imc <= 39.9:
        print('\033[1;30mObesidade Grau II\033[1;34m')
    else:
        print('\033[1;30mObesidade Grau III\033[1;34m')

    if b == c - 1:
        print(f'{"FIM DO PROGRAMA":=^45}')
    else:
        print('\033[1;34m=' * 45, '\033[1;30m')
