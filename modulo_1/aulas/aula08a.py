# Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {}' .format(num, math.ceil(raiz)))

# Importações Match

# math.ceil = aredondamento do número para cima.
# math.floor = aredondamento do número para baixo.
# math.trunc = vai trucar o número, sem fazer arredondamento, vai tirar os depois da vírgula.
# math.pow = potência.
# math.sqrt = calcular raiz quadrada.
# math.factorial = calcular fatorial do número.
