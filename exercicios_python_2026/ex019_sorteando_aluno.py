# Exercício 019 - Sorteando um aluno
# Sorteia aleatoriamente um aluno entre quatro nomes informados.

# Importa a biblioteca random para realizar o sorteio.
import random

# Solicita os nomes dos quatro alunos.
n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')

# Armazena os nomes dos alunos em uma lista.
lista = [n1,n2,n3,n4]

# Escolhe aleatoriamente um dos elementos da lista.
escolhido = random.choice(lista)

# Exibe o nome do aluno sorteado.
print('O aluno escolhido foi {}'.format(escolhido))


