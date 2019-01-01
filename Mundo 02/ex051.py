#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e
#a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('\033[1;35m--=DESAFIO 51=--')
primeirotermo = int(input('\033[1;33mDigite o primeiro termo: '))
razão = int(input('Digite a razão: \033[1;30m'))
for c in range(primeirotermo, primeirotermo + 10 * razão, razão):
    print(c, end=' → ')
