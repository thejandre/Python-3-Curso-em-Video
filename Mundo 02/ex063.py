#Exercício Python 063: Escreva um programa que leia um número
#N inteiro qualquer e mostre na tela os N primeiros elementos
#de uma Sequência de Fibonacci.
print('\033[1;31m--=DESAFIO 63=--') #FIBONACCI
contador = int(input('\033[1;33mDigite um número inteiro: \033[1;30m'))
a, b = 0, 1
while contador != 0:
    contador -= 1
    print(b, end=' → ')
    a, b = b, a + b
