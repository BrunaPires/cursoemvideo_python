# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(a))
print('Tem espaços: ', a.isspace())
print('É um número: ', a.isnumeric())
print('É alfabético: ', a.isalpha())
print('Está em letras maiúsculas: ', a.isupper())
print('Está em letras minuscúlas: ', a.islower())
print('Está capitalizada: ', a.istitle())
