#calcule a soma, subtração, multiplicação,divisão,potência, divisão inteira e resto da divisão
#de dois números digitados pelo usuário

n1 = int(input('Digite um valor '))
n2 = int(input('Digite outro valor '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2
divisao_inteira = n1 // n2
resto = n1 % n2

print('A operações efetuadas com {} e {} são :  soma  {}, subtração {}, multiplicação {}, divisão {}, potência {}, '
      'divisão inteira {} e resto da divisão {}'.format(n1, n2, soma, subtracao, multiplicacao, divisao, potencia,
                                                        divisao_inteira, resto))
