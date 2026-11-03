# Exercício 030 - Par ou ímpar
# Verifica se um número inteiro é par ou ímpar
# utilizando o operador de módulo e estruturas condicionais.

# Solicita um número inteiro ao usuário.
n = int(input('Me diga um numero: '))

# Verifica se o resto da divisão do número por 2 é igual a zero.
if n%2 == 0:
    # Se o resto for zero, o número é par.
    print('O numero {} é PAR'.format(n))
else:
    # Caso contrário, o número é ímpar.
    print('O numero {} é IMPAR'.format(n))
