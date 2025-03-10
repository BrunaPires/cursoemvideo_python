# Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um numero: '))
s = n1 + 1
a = n1 - 1

print('O numéro digitado foi {}' .format(n1))
print('O sucessor do numéro {} é {}' .format(n1, s))
print('O antecessor do numéro {} é {}' .format(n1, a))