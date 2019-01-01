#Exercício Python 010: Crie um programa que leia quanto dinheiro
#uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
print('\033[1;31m--=DESAFIO 10=--\033[m')
print('Vamos descobrir quantos dólares você pode comprar no momento.')
c = float(input('Quantos reais você possui? '))
d = c/3.27
print('No momento, é possível que você compre {:.2f} dólares!'.format(d))
