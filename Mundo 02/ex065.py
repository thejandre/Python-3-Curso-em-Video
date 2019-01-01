#Exercício Python 065: Crie um programa que leia vários números
#inteiros pelo teclado. No final da execução, mostre a média
#entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar
#a digitar valores.
print('\033[1;31m--=DESAFIO 65=--')
maior = soma = quantidade = menor = 0
continuar = 'S'
while continuar == 'S':
    valor = int(input('\033[1;33mDigite um valor: '))
    continuar = str(input('Deseja continuar digitando? [S/N] ')).upper().strip()
    quantidade += 1
    soma += valor
    if quantidade == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
if maior > menor:
    print('\033[1;30mO maior número é {} e o menor é {}, a média dos {} números digitados é {:.1f}.'.format(maior, menor, quantidade, soma / quantidade))
else:
    print('\033[1;30mNão há número maior nem menor, todos são iguais. A média dos {} números digitados é {:.1f}.'.format(quantidade, soma / quantidade))
