#Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
print('\033[1;36m--=DESAFIO 29=--\033[m')
velocidade = int(input('Você está passando por um radar. Qual sua velocidade atual, em km/h: '))
if velocidade >= 160:
    print('O DOBRO DA VELOCIDADE PERMITIDA? Não serás multado, está preso!')
elif velocidade > 80:
    multa = (velocidade-80)*7
    print('O limite era 80km/h, você foi pego! Fostes multado em R${:.2f}.'.format(multa))
else:
    print('Você está dentro do limite de velocidade. Obrigado por manter a ordem!')
