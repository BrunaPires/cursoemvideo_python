# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))

# Verificando menor valor
menor = n1
if n2<n1 and n2<n3:
   menor = n2
if n3<n1 and n3<n2:
   menor = n3
   
# Verificando maior valor
maior = n1
if n2>n1 and n2>n3:
   menor = n2
if n3>n1 and n3>n2:
   menor = n3
 
print ('O menor valor digitado foi {:.0f}' .format(menor))
print ('O maior valor digitado foi {:.0f}' .format(maior)) 



