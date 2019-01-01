#Exercício Python 062: Melhore o DESAFIO 061, perguntando
#para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.
print('\033[1;31m--=DESAFIO 62=--')
primeirotermo = int(input('\033[1;33mDigite o primeiro termo: '))
razão = int(input('Digite a razão: \033[1;30m'))
termos = 10
while termos != 0:
    print(primeirotermo, end=' → ')
    primeirotermo += razão
    termos -= 1
    if termos == 0:
        termos = int(input('\n\033[1;33mQuantos mais termos deseja visualizar? \033[1;31m(0 para nenhum) \033[1;30m'))
