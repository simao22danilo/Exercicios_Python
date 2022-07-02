## FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE
# ARTIFÍCIO, INDO DE 10 ATÉ 0, COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES. ##
from time import sleep
for cont in range(10, -1,-1):
    print(cont)
    sleep(1)
print('BUM! BUM! POOOW!')