#Exercício Python 053: Crie um programa que leia uma frase
#qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
print('\033[1;34m--=DESAFIO 53=--')
frase = str(input('\033[1;33mDigite uma frase: \033[1;30m')).replace(' ', '').upper().strip()
print('Frase ao contrário: ', frase[::-1])
print('Frase normal: ', frase)
if frase == frase[::-1]:
    print('Esta frase é um palíndromo.')
else:
    print('Esta frase não é um palíndromo.')
