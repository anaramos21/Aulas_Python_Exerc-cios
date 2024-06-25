#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

#formato matemático
'''co= float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi= (ca**2+co**2)**(1/2)
print('O valor da hipotenusa é {}'.format(hi))'''

import math
co= float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi=math.hypot(co,ca)
print('O valor da hipotenusa é {}'.format(hi))