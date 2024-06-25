#Diga se o valor digitado é numérico ou texto. Faça um teste para cada situação

print('------ valor numérico -------')
n1=(input('Digite um valor numérico: '))
print(n1.isnumeric())
print('')

print('------ valor texto -------')
n2=(input('Digite um outro valor, porém, que seja texto '))
print(n2.isalpha())
print('')