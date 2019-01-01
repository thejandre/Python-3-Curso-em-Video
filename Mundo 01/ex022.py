#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
print('\033[1;31m--=DESAFIO 22=--\033[m')
nome = input('Qual é o seu nome completo? ')
print('Nome em maiúsculo:',nome.upper())
print('Nome em minúsculo:',nome.lower())
dividido = nome.split()
primeironome = dividido[0]
print('Número de caracteres do primeiro nome:',len(primeironome))
print('Número de caracteres do nome completo:',len(nome))
print('Número de caracteres do nome completo, sem contar os espaços:',len(nome)-nome.count(' '))
