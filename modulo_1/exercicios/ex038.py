# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print('O PRIMEIRO valor é maior')
elif num1 < num2:
    print('O SEGUNDO valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
