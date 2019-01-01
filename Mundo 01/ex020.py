#Exercício Python 019: Um professor quer sortear um dos seus
#quatro alunos para apagar o quadro. Faça um programa que ajude
#ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import shuffle
print('\033[4;37m--=DESAFIO 20=--\033[m')
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('A ordem de apresentação será {}!'.format(alunos))
