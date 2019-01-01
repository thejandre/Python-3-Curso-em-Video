#Exercício Python 007: Desenvolva um programa que leia
#as duas notas de um aluno, calcule e mostre a sua média.
print('\033[1;31m--=DESAFIO 7=--\033[m')
print('Vamos ver qual foi a sua média neste bimestre :)')
n1 = float(input('Qual foi a sua nota na primeira prova? '))
n2 = float(input('Qual foi a sua nota na segunda prova? '))
n3 = float(input('Qual foi a sua nota na terceira prova? '))
m = (n1+n2+n3)/3
print('Sua média foi {}!'.format(m))
