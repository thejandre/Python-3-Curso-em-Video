#Exercício Python 005: Faça um programa que leia um número
#Inteiro e mostre na tela o seu sucessor e seu antecessor.
print('\033[1;35m--=DESAFIO 5=--\033[m')
n1 = int(input('Digite um número: '))
a = n1-1
s = n1+1
print('O antecessor de {} é {} e seu sucessor é {}!'.format (n1, a, s))
