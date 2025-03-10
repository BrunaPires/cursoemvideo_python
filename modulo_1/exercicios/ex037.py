# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n1 = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opçao = int(input('Sua opção: '))

if opçao == 1:
    print('{} convertido para BINÁRIO é igual a {}' .format(n1, bin(n1)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL é igual a {}' .format(n1, oct(n1)[2:]))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}' .format(n1, hex(n1)[2:]))
else:
    print('Opção iválida... TENTE NOVAMENTE!')

