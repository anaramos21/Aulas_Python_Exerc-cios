#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Digite seu nome: ')
print('Olá ', nome, ' seja bem-vindo(a)!')


print('')
print('-------- Outra Forma --------')


#Imprime o nome no tamanho e formato desejado para caber dentro das {}
print('É um prazer te conhecer, {}'.format(nome))
