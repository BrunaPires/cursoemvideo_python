# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')) .strip() .upper()

# leia uma frase pelo teclado
print ('Sua frase é: {}' .format(frase))

# mostre quantas vezes aparece a letra “A”
print ('Na sua frase aparede {} vezes a letra A'.format(frase.count('A')))

# em que posição ela aparece a primeira vez
print ('A primeira letra A apareceu na posição {}' .format(frase.find('A') + 1))

# em que posição ela aparece a última vez
print ('A última letra A apareceu na posição {}' .format(frase.rfind('A') + 1))

# print (frae[:5].upper() == 'SANTO') (frase.count('A'))
