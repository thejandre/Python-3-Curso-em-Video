#Exercício Python 015: Escreva um programa que pergunte a quantidade
#de Km percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
#custa R$60 por dia e R$0,15 por Km rodado.
print('\033[1;32m--=DESAFIO 15=--\033[m')
print('Obrigado por requisitar nossos serviços :) Para calcular-mos o total a pagar, responda as seguintes questões:')
kmpercorridos = float(input('Quantos kilometros você percorreu com o veículo? '))
dias = int(input('A quantos dias você está com o veículo? '))
print('O total a pagar é R${:.2f}. Volte sempre :D'.format((kmpercorridos * 0.15) + (dias * 60)))
