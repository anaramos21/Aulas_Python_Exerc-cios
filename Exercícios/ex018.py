#Escreva um programa que converta uma temperatura digitando em graus Celsius e
# converta para graus Fahrenheit.

temperatura=float(input('Digite a temperatura em graus Celsius '))
print('A temperatura de {}º é o equivalente em  {}F'.format(temperatura, ((temperatura*9)/5)+32))