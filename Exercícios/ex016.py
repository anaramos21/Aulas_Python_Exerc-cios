#faça um algoritmo que leia um valor e dê 5% de desconto sobre este e traga na tela para o
#usuário o novo valor

valor=float(input('Digite o valor desejado '))
print('O valor atual é R${:.2f} e com desconto ficará R${:.2f}'.format(valor, valor-(valor*0.05)))
