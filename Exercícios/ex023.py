#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angle= float(input('Digite o ângulo que você deseja: '))
sin= math.sin(math.radians(angle))
cos= math.cos(math.radians(angle))
tan= math.tan(math.radians(angle))
print('O ângulo {} tem o seno de {:.2f} , cosseno de {:.2f} e tangente de {:.2f}'.format(angle,sin,cos,tan))
