#Exercício Python 077: Crie um programa que tenha uma tupla com
#várias palavras (não usar acentos). Depois disso, você deve mostrar,
#para cada palavra, quais são as suas vogais.
print('\033[1;31m--=DESAFIO 77=--\033[1m')
palavras = ('aprender', 'programar', 'linguagem', 'python', 'gratis', 'praticar',
            'roacutan', 'manteiga', 'batata', 'fritar', 'vegano', 'futuro')
for p in palavras:
    print(f'\nNa palavra \033[1;30m{p.upper()}\033[1m temos', end=': ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[1;30m{letra}\033[1m', end=' ')
