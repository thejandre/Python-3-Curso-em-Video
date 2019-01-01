#Exercício Python 060: Faça um programa que leia
#um número qualquer e mostre o seu fatorial.
print('\033[1;31m--=DESAFIO 61==-')
primeirotermo = int(input('\033[1;33mDigite o primeiro termo: '))
razão = int(input('Digite a razão: \033[1;30m'))
contador = 10
while contador != 0:
    print(primeirotermo, end=' → ')
    primeirotermo += razão
    contador -= 1
