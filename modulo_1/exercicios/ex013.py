# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

funcionario = input('Digite seu nome: ')
salario = float(input('Informe seu salário atual R$ '))
novo = salario + (salario * 15 / 100)

print('{} você ganhava R${:.2f}, com 15% de aumento, seu novo salário será no valor de R${:.2f}' .format(funcionario, salario, novo))
      