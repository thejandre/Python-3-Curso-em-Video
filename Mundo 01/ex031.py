#Exercício Python 031: Desenvolva um programa que pergunte a distância
#de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
#Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
print('\033[1;31m--=DESAFIO 31=--\033[m')
viagem = int(input('Qual a distância em KM que você percorreu em sua viagem na nossa agência? '))
if viagem > 200:
    valor = viagem*0.45
else:
    valor = viagem*0.50
print('O valor de nossos serviços ficará por R${:.2f}. Obrigado pela preferência!'.format(valor))
