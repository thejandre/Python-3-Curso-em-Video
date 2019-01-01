#Exercício Python 012: Faça um algoritmo que leia o preço
#de um produto e mostre seu novo preço, com 5% de desconto.
print('\033[1;36m--=DESAFIO 12=--\033[m')
p = float(input('Digite o preço do produto que você deseja adicionar 5% de desconto: '))
d = p*5/100
r = p-d
print('O novo valor deste produto é {}. Aproveite o cupom :)'.format(r))
