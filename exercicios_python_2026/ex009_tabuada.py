# Exercício 009 - Tabuada de um número inteiro
# Objetivo: receber um número inteiro e exibir
# sua tabuada de multiplicação de 1 a 10.

n1 = int(input('Digite um numero para ver sua tabuada '))

# A multiplicação de uma string por 20 cria uma linha com 20 hífens,
# utilizada para separar visualmente a tabuada no terminal.
print('-'*20)

# O {:2} reserva uma largura mínima de dois caracteres,
# permitindo alinhar os multiplicadores da tabuada.
print('{} x {:2} = {}'.format(n1,1,n1*1))
print('{} x {:2} = {}'.format(n1,2,n1*2))
print('{} x {:2} = {}'.format(n1,3,n1*3))
print('{} x {:2} = {}'.format(n1,4,n1*4))
print('{} x {:2} = {}'.format(n1,5,n1*5))
print('{} x {:2} = {}'.format(n1,6,n1*6))
print('{} x {:2} = {}'.format(n1,7,n1*7))
print('{} x {:2} = {}'.format(n1,8,n1*8))
print('{} x {:2} = {}'.format(n1,9,n1*9))
print('{} x {:2} = {}'.format(n1,10,n1*10))

print('-'*20)
