# Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

frase = 'Curso em Video Python'

# Ler apenas a variável frase
print(frase)

# Fatiar "Ler apenas o conteúdo na posição 3"
print (frase[3])

# Fatiar "Ler apenas o conteúdo na posição 3 até o 13"
print (frase[3:13])

# Verificar quantas vezes aparece a letra desejada
print (frase.count('o'))

# Verificar qual é o tamanho da frase
print (len(frase))

# Trocar uma palavra da váriavel
print (frase.replace('Python', 'Android'))

# Trocar todas letras para maiúsculas
print (frase.upper())

# Trocar todas letras para minusculas
print (frase.lower())

# Separar elementos em listas
print (frase.split())

# Juntar elementos em listas
print ('-' .join(frase))

# Juntar elementos em listas
print (frase.title())


# Fazer a leitura de um texto grande
print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""")