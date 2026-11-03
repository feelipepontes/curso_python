# Exercício 020 - Sorteando uma ordem
# Define uma ordem aleatória de apresentação para quatro alunos.

# Importa a biblioteca random para realizar o embaralhamento.
import random

# Solicita os nomes dos quatro alunos.
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

# Armazena os nomes dos alunos em uma lista.
lista= [n1,n2,n3,n4]

# Embaralha aleatoriamente a ordem dos elementos da lista.
random.shuffle(lista)

# Exibe a ordem de apresentação após o embaralhamento.
print('A ordem de apresentação será: ')
print(lista)
