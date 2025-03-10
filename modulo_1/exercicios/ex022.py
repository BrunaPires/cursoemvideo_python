# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Digite seu nome completo: ')) .strip()
print('Analisando seu nome...')

# O nome com todas as letras maiúsculas.
print('Seu nome em letras maiúsculas é {}.' .format(nome.upper()))

# O nome com todas as letras minúsculas.
print('Seu nome em letras minúsculas é {}.' .format(nome.lower()))

# Quantas letras ao todo (sem considerar espaços)
print('Seu nome completo tem ao todo {} letras' .format(len(nome) - nome.count(' ')))

# Quantas letras tem o primeiro nome.
separa = nome.split() # Aqui ele está separando palavras da frase
print('Seu primeiro nome é {} e ele tem {} letras' .format(separa[0], nome.find(' ')))
