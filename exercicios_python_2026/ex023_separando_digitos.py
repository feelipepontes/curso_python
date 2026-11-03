# Exercício 023 - Separando dígitos de um número
# Identifica os algarismos da unidade, dezena, centena e milhar
# utilizando divisão inteira e o operador de módulo.

# Solicita um número inteiro ao usuário.
n1 = int(input('Insira um numero: '))

# Obtém o algarismo da unidade.
u = n1 // 1 % 10

# Obtém o algarismo da dezena.
d = n1 // 10 % 10

# Obtém o algarismo da centena.
c = n1 // 100 % 10

# Obtém o algarismo da unidade de milhar.
m = n1 // 1000 % 10

# Exibe o número original e os algarismos identificados.
print('Analisando o numero {}'.format(n1))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
