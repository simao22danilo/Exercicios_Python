## DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU IMC E MOSTRE
# SEU STATUS, DE ACORDO COM A TABELA ABAIXO:
# - ABAIXO DE 18.5: ABAIXO DO PESO
# - ENTRE 18.5 E 25: PESO IDELA
# - 25 ATÉ 30: SOBREPESO
# - 30 ATÉ 40: OBSEIDADE
# - ACIMA DE 40: OBESIDADE MÓRBIDA ##
peso = float(input('Qaul é seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO DO PESO  normal')
elif 18.5 <= imc <25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc <30:
    print('Você está em SOBREPESO')
elif 30 <= imc <40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
