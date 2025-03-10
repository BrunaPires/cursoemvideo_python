# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
a1 = str(input('Primeiro(a) aluno(a): '))
a2 = str(input('Segundo(a) aluno(a): '))
a3 = str(input('Tericeiro(a) aluno(a): '))
a4 = str(input('Quarto(a) aluno(a): '))
lista = [a1, a2, a3, a4]
aluno = choice(lista)

print ('O(a) aluno(a) escolhido(a) foi {}' .format(aluno))








