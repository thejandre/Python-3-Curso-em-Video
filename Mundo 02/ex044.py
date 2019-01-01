#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura
#de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
#mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
print('\033[1;31m--=DESAFIO 44=--\033[m')
preço = float(input('\033[1;33mDigite o preço do produto: R$\033[m'))
print('\033[1;31mQual método de pagamento deseja usar?\033[m')
print('Digite 1 para à vista em dinheiro e receba 10% de desconto.')
print('Digite 2 para à vista no cartão e receba 5% de desconto.')
print('Digite 3 para em até 2x no cartão e pague o preço normal.')
print('Digite 4 para pagar em 3x ou mais no cartão e pague 20% de juros.')
pagamento = int(input('\033[1;33mEscolha uma das opções acima: \033[m'))
if pagamento == 1:
    desconto = preço - (preço * 10 / 100)
    print('Você escolheu pagar à vista em dinheiro e recebeu 10% de desconto. \nVocê poupou R${:.2f} e pagará somente R${:.2f} :)'.format (preço * 10 / 100, desconto))
elif pagamento == 2:
    desconto = preço - (preço * 5 / 100)
    print('Você escolheu pagar à vista no cartão e recebeu 5% de desconto. \nVocê poupou R${:.2f} e pagará somente R${:.2f} :)'.format(preço * 5 / 100, desconto))
elif pagamento == 3:
    print('Neste método de pagamento você não recebe desconto. \nPagará o preço normal de R${:.2f}.'.format(preço))
elif pagamento == 4:
    print('Escolheu a opção 3x no cartão e terá que pagar 20% de juros. \nO novo valor do produto é R${:.2f}.'.format(preço + (preço * 20 / 100)))
else:
    print('Opção de pagamento inválida, tente novamente.')
