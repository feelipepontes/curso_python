# Exercício 013 - Reajuste salarial
# Calcula o novo salário de um funcionário após um aumento percentual.

# Solicita o salário atual do funcionário.
salário = float(input('Qual o salário de um funcionário? R$: '))

# Solicita a porcentagem de aumento salarial.
porcentagem = float(input('Quantos % de aumento o funcionário vai ter?: '))

# Calcula o valor do aumento com base na porcentagem informada.
aumento = salário*porcentagem/100

# Soma o aumento ao salário original para obter o novo salário.
novo = salário+aumento

# Exibe o salário original, a porcentagem de aumento e o novo salário.
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(salário,porcentagem,novo))

