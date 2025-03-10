# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um numero: '))
d = n1 * 2
t = n1 * 3
rq = n1 ** (1/2)

print('O numéro digitado foi {}' .format(n1))
print('O dobro do numéro {} é {}' .format(n1, d))
print('O triplo do numéro {} é {}' .format(n1, t))
print('O raiz quadrada do numéro {} é {:.2f}' .format(n1, rq))
