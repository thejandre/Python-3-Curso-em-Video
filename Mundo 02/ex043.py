#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura
#de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
#mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
print('\033[1;31m--=DESAFIO=--\033[m')
print('Vamos calcular o seu IMC!')
peso = float(input('Informe o seu peso em kilos: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal.')
elif imc > 25 and imc <= 30:
    print('Você está em sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Perigo! Você apresenta obesidade!')
else:
    print('Perigo extremo! Você apresenta obesidade mórbida!')
print('Seu IMC é {:.1f}'.format(imc))
