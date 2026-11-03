# Exercício 035 - Analisando triângulos
# Verifica se três segmentos de reta podem formar um triângulo
# utilizando a condição de existência de um triângulo.

# Exibe o título do programa.
print('Analisador de triângulos')

# Solicita as medidas dos três segmentos.
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

# Verifica se cada segmento é menor que a soma dos outros dois.
# Todas as condições precisam ser verdadeiras para formar um triângulo.
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    # Informa que os segmentos podem formar um triângulo.
    print('Os segmentos podem formar um triangulo')
else:
    # Informa que os segmentos não podem formar um triângulo.
    print('Os segmentos não podem formar um triangulo')
