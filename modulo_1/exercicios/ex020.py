# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a1 = str(input('Primeiro(a) aluno(a): '))
a2 = str(input('Segundo(a) aluno(a): '))
a3 = str(input('Tericeiro(a) aluno(a): '))
a4 = str(input('Quarto(a) aluno(a): '))
lista = [a1, a2, a3, a4]
shuffle(lista)

print ('A ordem de apresentação será: \n{}' .format(lista))








