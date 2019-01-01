#Exercício Python 037: Escreva um programa em Python que leia um número inteiro
#qualquer e peça para o usuário escolher qual será a base de conversão: 1 para
#binário, 2 para octal e 3 para hexadecimal.
print('\033[1;31m--=DESAFIO 37=--\033[m')
num = int(input('\033[1;33mDigite um número inteiro: '))
print('\033[1;33mEscolha uma opção de conversão;')
print('''\033[1;30m[1]\033[m BINARIO
\033[30;1m[2]\033[m OCTAL
\033[30;1m[3]\033[m HEXADECIMAL''')
opção = int(input('\033[1;33mDigite sua opção: \033[1;30m'))
if opção == 1:
    print('O número {} para binário é {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} para octal é {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para hexadecimal é {}.'.format(num, hex(num)[2:]))
