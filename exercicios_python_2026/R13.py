salário= float(input('Qual o salário de um funcionário? R$: '))
porcentagem= float(input('Quantos % de aumento o funcionário vai ter?: '))
aumento= salário*porcentagem/100
novo= salário+aumento
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(salário,porcentagem,novo))
