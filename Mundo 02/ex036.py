#Exercício Python 036: Escreva um programa para aprovar o empréstimo
#bancário para a compra de uma casa. Pergunte o valor da casa, o salário
#do comprador e em quantos anos ele vai pagar. A prestação mensal não pode
#exceder 30% do salário ou então o empréstimo será negado.
print('\033[1;31m--=DESAFIO 36=--\033[m')
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário mensal: '))
tempo = int(input('Digite a quantidade de anos que pretende levar para pagar: '))
prestação = casa / (tempo * 12)
porcentagem = 30 * salario / 100
if porcentagem < prestação:
    print('Infelizmente seu empréstimo foi negado.')
else:
    print('Parabéns, conseguiu o empréstimo! Terá que pagar R${:.2f} por mês durante {} meses.'.format(prestação, tempo * 12))
