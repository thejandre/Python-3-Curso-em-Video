'''     Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''


def escreva(txt):
    print('\033[1;34m-' * int(len(txt) + 2))
    print(f'\033[1m {txt}')
    print('\033[1;34m-' * int(len(txt) + 2))


print('\033[1;31m--=DESAFIO 97=--\033[1m')
while True:
    escreva(input('\033[1mEscreva uma frase: '))
    continuar = input('\033[1mDeseja continuar? [S/N]: ').upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = input('\033[1;31mErro!\033[1m Deseja continuar? [S/N]: ').upper().strip()
        if continuar == 'N':
            break
    if continuar == 'N':
        break
print(f'\033[1;34m{"FIM DO PROGRAMA":=^31}')
