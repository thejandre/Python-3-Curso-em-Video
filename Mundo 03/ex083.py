#Exercício Python 083: Crie um programa onde o usuário digite uma expressão
#qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão
#passada está com os parênteses abertos e fechados na ordem correta.
print('\033[1;31m--=DESAFIO 83=--\033[1m')
expressão = input('Digite uma expressão com parênteses: ')
p1 = p2 = 0
for letra in expressão:
    if letra == '(':
        p1 += 1
    elif letra == ')':
        p2 += 1
if p1 == p2:
    print('Expressão válida.')
else:
    print('Expressão inválida.')
