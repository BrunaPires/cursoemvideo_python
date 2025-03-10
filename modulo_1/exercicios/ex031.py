# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual é a distância da sua viagem? '))
viagem_curta = distancia * 0.50
viagem_longa = distancia * 0.45

if distancia <= 200: 
    print ('Você está prestes a começar uma viagem de {:.0f}Km. \nE o preço da sua passagem será de R${:.2f}' .format(distancia,viagem_curta)) 
else:
    print ('Você está prestes a começar uma viagem de {:.0f}Km. \nE o preço da sua passagem será de R${:.2f}' .format(distancia,viagem_longa)) 
