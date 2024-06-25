#crie um algoritmo que leia um número e mosre seu dobro, triplo e sua raiz quadrada.

num = int(input('Digite um número '))
print('O dobro desse número é {} , o triplo é {} e a sua raiz quadrada desse número é {:.3f}'.format(num*2,num*3, num**(1/2)))