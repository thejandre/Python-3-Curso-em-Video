#Exercício Python 013: Faça um algoritmo que leia o salário
#de um funcionário e mostre seu novo salário, com 15% de aumento.
print('\033[1;31m--=DESAFIO 13=--\033[m')
print('Você foi promovido! De acordo com as normas da empresa, recebestes 15% de aumento.')
s = float(input('Digite o seu salário atual para calcularmos o seu novo salário: '))
p = s*15/100
ns = s+p
print('Parabéns! O seu novo salário é R${:.2f}!'.format(ns))
