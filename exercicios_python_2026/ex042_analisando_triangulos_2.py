# Exercício 042 - Analisando triângulos 2.0
# Verifica se três segmentos podem formar um triângulo
# e classifica o triângulo conforme as medidas dos lados.

# Solicita as medidas dos três segmentos.
n1 = float(input('Primeira reta: '))
n2 = float(input('Segunda reta: '))
n3 = float(input('Terceira reta: '))

# Verifica a condição de existência de um triângulo.
# A soma de quaisquer dois lados deve ser maior que o terceiro.
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('As retas podem formar um triângulo!')

    # Verifica se os três lados possuem a mesma medida.
    if n1 == n2 == n3:
        triangulo = 'equilátero'

    # Verifica se pelo menos dois lados possuem a mesma medida.
    elif n1 == n2 or n1 == n3 or n2 == n3:
        triangulo = 'isósceles'

    # Caso os lados sejam diferentes, o triângulo é escaleno.
    else:
        triangulo = 'escaleno'

    # Exibe a classificação do triângulo.
    print('As retas formam um triângulo {}'.format(triangulo))

# Executa este bloco caso os segmentos não formem um triângulo.
else:
    print('As retas não podem formar um triângulo!')



