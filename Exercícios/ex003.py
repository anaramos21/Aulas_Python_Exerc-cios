#digite dois valores, traga na tela e após efetue a soma e diga ao usuário o resultado da operação

#uma forma de fazer
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('O valores digitados são: ', n1, ' e ', n2)
soma = n1 + n2
print('')
print('O resultado da soma desses dois números é ', soma)


print('')
print('--------------outra forma -------------')

#formato mais profissional de responder
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('O valores digitados são: {} e {}'.format(n1,n2))
soma = n1 + n2
print('')
print('O resultado da soma desses dois números é {}'.format(soma))


