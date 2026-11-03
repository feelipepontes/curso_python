# Exercício 016 - Quebrando um número
# Exibe a parte inteira de um número real utilizando
# a conversão int() e a função math.trunc().

# Importa a biblioteca math para utilizar suas funções matemáticas.
import math

# Solicita um número real ao usuário.
num = float(input('Digite um valor: '))

# Converte o número para inteiro, descartando a parte decimal.
inteiro = int(num)

# Exibe o número original e sua parte inteira utilizando int().
print('O valor digitado foi {} e sua porção inteira é {}'.format(num,inteiro))

# Exibe o mesmo resultado utilizando a função math.trunc().
print('O valor digitado foi {} e sua porção inteira é {}'.format(num,math.trunc(num)))


