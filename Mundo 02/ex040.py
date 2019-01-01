#Exercício Python 040: Crie um programa que leia duas notas de um aluno e
#calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO
print('\033[1;31m--=DESAFIO 40=--\033[m')

print('\033[1;31mATENÇÃO!\033[1;33m Suas notas devem ser digitadas numa escala de 0 a 10.\033[m')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
média = (nota1 + nota2) / 2
print('Se suas notas foram {:.1f} e {:.1f}, sua média é {:.1f}.'.format(nota1, nota2, média))
if média < 5:
    print('\033[31mReprovado.')
elif média < 7 and média >= 5:
    print('\033[33mVocê ficou de recuperação!')
elif média >= 7:
    print('\033[32mAprovado!')
