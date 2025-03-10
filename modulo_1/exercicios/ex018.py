# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan 
a = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format (a, s))
c = cos (radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format (a, c))
t = tan (radians(a))
print('O ângulo de {} tem o TANGETE de {:.2f}'.format (a, t))








