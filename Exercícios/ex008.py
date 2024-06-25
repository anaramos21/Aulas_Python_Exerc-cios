#faça a divisão após a soma de dois números pelo último número digitado.
# O resultado deve possuir três casas decimais

n1 = int(input('Digite um valor '))
n2 = int(input('Digite outro valor '))
print('A soma desses dois valores é {}'.format(n1 + n2))
print("O resultado da operação é {:.3f}".format((n1 + n2) / n2))
