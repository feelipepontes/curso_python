# Exercício 017 - Catetos e hipotenusa
# Calcula a hipotenusa de um triângulo retângulo utilizando
# o Teorema de Pitágoras e a função math.hypot().

# Importa a biblioteca math para utilizar funções matemáticas.
import math

# Solicita os comprimentos dos catetos oposto e adjacente.
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

# Calcula a hipotenusa utilizando o Teorema de Pitágoras.
# A soma dos quadrados dos catetos é elevada a 1/2 para obter a raiz quadrada.
hip = (co**2 + ca**2)**(1/2)

# Calcula e exibe a hipotenusa utilizando a função math.hypot().
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(co,ca)))

# Exibe a hipotenusa calculada anteriormente pelo Teorema de Pitágoras.
print('A hipotenusa vai medir {:.2f}'.format(hip))
