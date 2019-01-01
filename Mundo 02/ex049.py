#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada
#de um número que o usuário escolher, só que agora utilizando um laço for.
print('\033[1;31m--=DESAFIO 49=--')
número = int(input('\033[1;33mDigite o número que você deseja saber a tabuada: '))
for c in range(1 , 10):
    print('\033[1;30m{} x {} = {}'.format(número, c, número * c))
