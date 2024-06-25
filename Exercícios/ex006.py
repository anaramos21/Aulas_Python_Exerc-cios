#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
# as informações possíveis sobre ele.

a = input('Digite algo ')
print('O tipo primitivo do que foi digitado é ', type(a))
print('É somente espaço? ', a.isspace())
print('É numérico?',a.isnumeric())
print('É do tipo string?', a.isalpha())
print('É alfanumérico?',a.isalnum())
print('Esta em caixa alta?', a.isupper())
print('Esta em caixa baixa?', a.islower())

