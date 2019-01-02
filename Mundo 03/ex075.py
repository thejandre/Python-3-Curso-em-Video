#Exercício Python 075: Desenvolva um programa que leia quatro
#valores pelo teclado e guarde-os em uma tupla. No final, mostre:
print('\033[1;31m--=DESAFIO 75=--\033[1m')
tupla = (int(input('Digite um valor: ')),
int(input('Digite outro valor: ')),
int(input('Digite mais um valor: ')),
int(input('Digite o último valor: ')))
print(f'Você digitou os valores {tupla}')
if tupla.count(9) == 0:
    print(f'O valor 9 não foi digitado nenhuma vez.')
elif tupla.count(9) > 1:
    print(f'O valor 9 foi digitado {tupla.count(9)} vezes.')
else:
    print(f'O valor 9 foi digitado apenas uma vez.')
if 3 not in tupla:
    print('O valor 3 não foi digitado nenhuma vez.')
else:
    print(f'O primeiro valor 3 digitado aparece na {tupla.index(3) + 1}ª posição.')
if tupla[0] % 2 == 0 or tupla[1] % 2 == 0 or tupla[2] % 2 == 0 or tupla[3] % 2 == 0:
    print('Os valores pares digitados foram:',
          tupla[0] if tupla[0] % 2 == 0 else '',
          tupla[1] if tupla[1] % 2 == 0 else '',
          tupla[2] if tupla[2] % 2 == 0 else '',
          tupla[3] if tupla[3] % 2 == 0 else '')
else:
    print('Nenhum número par digitado.')
