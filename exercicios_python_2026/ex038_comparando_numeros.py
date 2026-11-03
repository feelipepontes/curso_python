# Exercício 038 - Comparando números
# Compara dois números inteiros para identificar
# qual é o maior ou se ambos possuem o mesmo valor.

# Solicita dois números inteiros ao usuário.
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))

# Verifica se o primeiro número é maior que o segundo.
if n1 > n2:
    print('O PRIMEIRO numero é maior')

# Verifica se o primeiro número é menor que o segundo.
elif n1 < n2:
    print('O SEGUNDO numero é maior')

# Caso nenhuma das condições anteriores seja verdadeira,
# os dois números são iguais.
else:
    print('Os dois numeros são IGUAIS')
