## ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM:
# O PRIMEIRO VALOR É MAIOR
# O SEGUNDO VALOR É MAIOR
# NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS##
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo Número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Os dois valores são IGUAIS')
