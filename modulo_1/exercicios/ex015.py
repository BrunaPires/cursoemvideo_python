# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = float(input('Quantos dias o carro foi alugado? ')) 
km = float(input('Quantos KM rodado? KM '))
aluguel = (dias * 60) 
kilometros = (km * 0.15)
gasolina = aluguel + kilometros

print('O total a pagar é de R${:.2f}' .format(gasolina))