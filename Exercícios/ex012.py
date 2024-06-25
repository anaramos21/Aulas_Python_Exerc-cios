#faça um programa que leia valores em metros e o exiba convertido em centímetros e milímetros

valor=float(input('Digite o valor em metros '))
centimetros= valor*100
milimetros = valor*1000
print('O valor de {}m em centímetros é {}cm e em milímetros é {}mm'.format(valor,centimetros,milimetros))