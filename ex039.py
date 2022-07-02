## FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE, SE ELE AINDA VAI SE
# ALISTAR AO SERVIÇO MILITAR, SE É A HORA DE SE ALISTAR OU SE JÁ PASSOU DO TEMPO DO ALISTAMENTO. SEU PROGRAMA TAMBÉM
# DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO. ##
from datetime import date
atual = date.today().year
sexo = str(input('Digite "H" caso você seja homem ou "M" caso seja mulher: ')).upper().strip()
if sexo == 'M':
    print('Você não é obrigada a se alistar.')
else:
    nasc = int(input("Ano de nascimento: "))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}'.format(ano))
