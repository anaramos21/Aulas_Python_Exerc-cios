#faça um programa que receba o nome de um estudante , duas notas e diga a média ara o estudante com até duas casas decimais.

nome = input('Digite seu nome ')
n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
print('A média de {} é {:.2f}'.format(nome, (n1 + n2) / 2))
