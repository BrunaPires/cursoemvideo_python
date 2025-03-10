# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = float(input('Distância em metros: '))
cm = n1 * 100
mm = n1 * 1000

print('A medida de {}m, corresponde a {:.0f}cm e {:.0f}mm' .format(n1, cm, mm))

