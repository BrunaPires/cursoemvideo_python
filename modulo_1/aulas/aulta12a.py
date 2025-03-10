nome = str(input('Qual é seu nome? '))
if nome == 'Bruna':
    print( 'Que nome lindo!')
elif nome == 'João' or nome == 'Maria' or nome == 'José':
    print('Seu nome é popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um ótimo dia, {}!' .format(nome))