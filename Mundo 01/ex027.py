#Exercício Python 027: Faça um programa que leia o nome completo
#de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
print('\033[1;35m--=DESAFIO 27=--\033[m')
nome = input('Digite seu nome completo: ').title().strip().split()

print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))
