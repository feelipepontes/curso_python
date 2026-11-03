# Exercício 027 - Primeiro e último nome
# Identifica o primeiro e o último nome de uma pessoa
# a partir de seu nome completo.

# Solicita o nome completo e remove espaços das extremidades.
nome = str(input('Digite seu nome completo: ')).strip()

# Divide o nome em uma lista, separando as palavras pelos espaços.
nomes = nome.split()

# Exibe uma mensagem de apresentação.
print('Muito prazer em te conhecer!')

# Exibe o primeiro elemento da lista, localizado no índice 0.
print('Seu primeiro nome é {}'.format(nomes[0]))

# Exibe o último elemento da lista utilizando seu tamanho.
print('Seu ultimo nome é {}'.format(nomes[len(nomes)-1]))

