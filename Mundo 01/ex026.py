#Exercício Python 026: Faça um programa que leia uma frase
#pelo teclado e mostre quantas vezes aparece a letra "A",
#em que posição ela aparece a primeira vez e em que
#posição ela aparece a última vez.
print('\033[1;34m--=DESAFIO 26=--\033[m')
frase = str(input('Digite uma frase: ').upper().strip())
frase = frase.replace('Á','A')
frase = frase.replace('Ã','A')
frase = frase.replace('Ä','A')
frase = frase.replace('À','A')
frase = frase.replace('Â','A')
print('Quantas vezes a letra "A" aparece na frase:', frase.count('A'))
primeiroa = frase.find('A')
segundoa = frase.rfind('A')
primeiroa = primeiroa+1
segundoa = segundoa+1
print('A letra "A" aparece, primeiramente, no espaço {}, em seguida, no espaço {}!'.format(primeiroa, segundoa))
