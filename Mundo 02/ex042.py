#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando
#o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
print('\033[1;32m--=DESAFIO 42=--\033[m')
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 > r2 - r3 and r2 > r1 - r3 and r3 > r1 - r2:
    if r1 == r2 and r1 == r3:
        print('As 3 retas formam um triângulo equilátero.')
    elif r1 == r2 and r1 != r3:
        print('As 3 retas formam um triângulo isósceles.')
    elif r2 == r3 and r1 != r2:
        print('As 3 retas formam um triângulo isósceles.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('As 3 retas formam um triângulo escaleno.')
else:
    print('As 3 retas não formam um triângulo.')
