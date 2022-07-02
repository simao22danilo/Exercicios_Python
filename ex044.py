## ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO
# NORMAL E CONDIÇÃO DE PAGAMENTO:
# - À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
# - À VISTA NO CARTÃO: 5% DE DESCONTO
# - EM ATÉ 2 X NO CARTÃO: PREÇO NORMAL
# - 3 X OU MAIS NO CARTÃO 20% DE JUROS ##
print('{:=^40}'.format(' LOJAS SD '))
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcela em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preco
    print('\033[1;31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')
print('Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(preco, total))
