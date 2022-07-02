## ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E MILÍMETROS. ##
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10

print(f'A medida de {medida} m (metros) corresponde a: \n{medida / 1000} km (quilômetros) \n{medida * 10} hm (hectômetros) \n{medida / 10} dam (decâmetros)\n{medida * 10} dm (decímetros)\n{medida * 100} cm (centímetros)\n{medida * 1000} mm (milímetros)')