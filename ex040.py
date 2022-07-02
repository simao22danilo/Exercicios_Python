## CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA  MENSAGEM
# NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA:
# - MÉDIA ABAIXO DE 5.0: REPROVADO
# - MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
# - MÉDIA 7.0 OU SUPERIOR: APROVADO ##
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segundanota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media >=5 and media <7:
    print('O aluno está em RECUPERAÇÃO.')
elif media<5:
    print('O aluno está REPROVADO.')
elif media >=7:
    print('O aluno está APROVADO')