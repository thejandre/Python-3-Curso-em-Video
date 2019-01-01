#Exercício Python 008: Escreva um programa que leia um valor
#em metros e o exiba convertido em centímetros e milímetros.
print('\033[1;36m--=DESAFIO 8=--\033[m')
m = float(input('Qual a sua altura em metros? '))
c = int(m*100)
m1 = int(c*10)
print('Se você possui {} metros de altura, isto significa que:'.format(m))
print('Você possui {}cm de altura ou {}mm!'.format(c, m1))
