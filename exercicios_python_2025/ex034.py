salário = float(input('Qual o seu salario?: R$'))
if salário > 1250.00:
    salário = salário * 10 / 100 + salário
    print('Houve um aumento de 10% no seu salario, agora ele é de {:.2f}: '.format(salário))
elif salário <= 1250.00:
    salário = salário * 15 / 100 + salário
    print('Houve um aumento de 15% no seu salário, agora ele é de {:.2f}: '.format(salário))
## Os dois fazem a mesma coisa só que um usa elif e o outro else ##
salário = float(input('Qual o seu salario'))
if salário >= 1250.00:
    novo = salário * 10 / 100 + salário
    print('Seu novo salário é de R$ {}'.format(novo))
else:
    novo = salário * 15 / 100 + salário
    print('Seu novo salário é de R$ {}'.format(novo))

