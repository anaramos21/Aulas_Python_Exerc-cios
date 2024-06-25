#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

km = float(input('Digite quantos km você deseja andar com o carro alugado '))
qtd_dias = (float(input('Digite quantos dias deseja ficar com o carro ')))
preco_a_pagar = ((60 * qtd_dias) + (0.15 * km))

print('O valor a ser pago no final será de R${:.2f} para {} km rodados em {} dias'.format(preco_a_pagar, km, qtd_dias))
