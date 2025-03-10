# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real= float(input('Quanto dinheiro você tem na cateira? R$'))
dolar = real / 5.696

print('Com R${:.2f} no dia 21/02/2025 você pode comprar US${:.2f}' .format(real, dolar))