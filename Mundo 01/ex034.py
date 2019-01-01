#Exercício Python 034: Escreva um programa que pergunte o salário de um
#funcionário e calcule o valor do seu aumento. Para salários superiores
#a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
#o aumento é de 15%.
print('\033[1;31m--=DESAFIO 34=--\033[m')
salario = float(input('Qual o seu salário atual: '))
if salario > 1250:
    print('Com base em nosso sistema, seu aumento será de 10% e seu novo salário será R${:.2f}'.format(salario*1.1))
elif salario <= 1250:
    print('Com base em nosso sistema, seu aumento será de 15% e seu novo salário será R${:.2f}'.format(salario*1.15))
