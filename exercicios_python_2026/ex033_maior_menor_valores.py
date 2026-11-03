# Exercício 033 - Maior e menor valores
# Identifica o maior e o menor entre três números inteiros,
# utilizando comparações e estruturas condicionais.

# Solicita três números inteiros ao usuário.
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

# Considera inicialmente o primeiro número como o menor.
menor = n1

# Verifica se o segundo número é menor que os outros dois.
if n2 < n1 and n2 < n3:
    menor = n2

# Verifica se o terceiro número é menor que os outros dois.
if n3 < n1 and n3 < n2:
    menor = n3

# Considera inicialmente o primeiro número como o maior.
maior = n1

# Verifica se o segundo número é maior que os outros dois.
if n2 > n1 and n2 > n3:
    maior = n2

# Verifica se o terceiro número é maior que os outros dois.
if n3 > n1 and n3 > n2:
    maior = n3

# Exibe o menor e o maior valor encontrados.
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))





