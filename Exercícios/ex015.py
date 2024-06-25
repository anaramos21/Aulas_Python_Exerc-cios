#Faça um programa que leia a largura e altura de uma parede em emtros e calcule a sua área,
#perímetro. Diga quantos litros de tinta são necessários para pintar toda essa parede, sabendo
#de que cada litro de tinta pinta 2m2

largura= float(input('Digite o valor da largura '))
altura=float(input('Digite o valor da altura '))

print('Para a área de {}m2 dessa parede, necessita-se {}l de tintas. '.format(largura*altura,(largura*altura)/2))

