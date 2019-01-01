#Exercício Python 014: Escreva um programa que converta uma temperatura
#digitando em graus Celsius e converta para graus Fahrenheit.
print('\033[1;31m--=DESAFIO 14=--\033[m')
print('Vamos converter Celsius para Fahrenheit.')
c = float(input('Digite a temperatura em  °C: '))
print('Temos {:.1f}°F'.format(c * 1.8 + 32))
