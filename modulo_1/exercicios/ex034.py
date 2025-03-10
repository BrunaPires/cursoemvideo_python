# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o salário do funcionário? R$ '))

# aumento de 10%
if salario >= 1250:
   aumento1 = salario + (salario * 10 / 100)
   print ('Quem ganhava R${:.2f} com 10% de aumento, passa a ganhar R${:.2f} agora.' .format(salario, aumento1))
# aumento é de 15%
else:
   aumento2 = salario + (salario * 15 / 100)
   print ('Quem ganhava R${:.2f} com 15% de aumento, passa a ganhar R${:.2f} agora.' .format(salario, aumento2))



