#faça um conversor de moeda de $ para R$

dinheiro=float(input('Digite o valor em R$ que vc deseja converter para $ '))

#1$ é igual a R$5,36

print ('O valor de R${:.2f} convertido para dólares é o equivalente a ${:.2f}'.format(dinheiro, dinheiro/5.36))
