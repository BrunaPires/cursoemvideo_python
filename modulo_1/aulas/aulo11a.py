# Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.

# =================================================

# Cores no terminal
#     \033[0;33;44m 

# =================================================

# Estilos
# 0 - None
# 1 - Bold
# 4 - Underline
# 7 - Negative

# =================================================

# Cores de Texto
# 30 - Branco
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul
# 35 - Roxo
# 36 - Azul água
# 37 - Cinza

# =================================================

# Cores de Fundo
# 40 - Branco
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelo
# 44 - Azul
# 45 - Roxo
# 46 - Azul água
# 47 - Cinza

# =================================================

# Exemplo
frase = 'Olá teste'
print('{}}'.format(frase, '\033[0;33;44'))
