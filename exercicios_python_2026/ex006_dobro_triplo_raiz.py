# Exercício 006 - dobro, triplo e raiz quadrada
# Objetivo: receber um numero inteiro e calcular seu dobro,
# triplo e raiz quadrada, exibindo os resultados em linhas separadas

n1 = int(input('Digite um numero: '))

# O \n permite quebrar a linha dentro de uma string,
# sem precisar utilizar vários comandos print().
print('O dobro de {} é {} \nO triplo de {} é {} \nA raiz quadrada de {} é {}'.format(n1,n1*2,n1,n1*3,n1,n1**(1/2)))
