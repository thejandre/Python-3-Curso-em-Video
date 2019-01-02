#Exercício Python 090: Faça um programa que leia nome e
#média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.
print('\033[1;31m--=DESAFIO 90=--\033[1m')
aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('\033[1;34m-' * 21)
print(f'\033[1mNome: {aluno["nome"]} ')
print(f'Média: {aluno["média"]}')
if aluno['média'] >= 5:
    print(f'\033[1;32m{"APROVADO!":^21}')
else:
    print(f'\033[1;31m{"REPROVADO!":^21}')
print('\033[1;34m-' * 21)
