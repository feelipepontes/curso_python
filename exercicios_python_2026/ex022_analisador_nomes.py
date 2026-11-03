# Exercício 022 - Analisador de nomes
# Analisa um nome completo, exibindo suas versões em maiúsculas
# e minúsculas, a quantidade de letras e o tamanho do primeiro nome.

# Solicita o nome completo e remove espaços no início e no final.
nome = str(input('Digite o seu nome completo: ')).strip()

# Exibe uma mensagem indicando o início da análise.
print('Analisando o seu nome ...')

# Converte todas as letras do nome para maiúsculas.
print('Seu nome em maiúsculas é {}'.format(nome.upper()))

# Converte todas as letras do nome para minúsculas.
print('Seu nome em minúsculas é {}'.format(nome.lower()))

# Conta os caracteres do nome, desconsiderando os espaços comuns.
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

# Localiza o primeiro espaço para determinar o tamanho do primeiro nome.
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))


