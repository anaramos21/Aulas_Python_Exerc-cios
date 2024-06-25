#faça um algoritmo que leia o salário de um funcionario e acrescente 15% do valor
#imprima na tela o novo valor

v_inicial_salario=float(input('Digite o valor do salário do funcionário '))
v_final_salario=v_inicial_salario+(v_inicial_salario*0.15)
print('O salário inicial era de R${:.2f} e após o aumento recevido passou a ser R${:.2f}'.format(v_inicial_salario,v_final_salario))