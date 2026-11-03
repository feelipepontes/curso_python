# Exercício 036 - Aprovando empréstimo
# Simula a aprovação de um empréstimo imobiliário,
# verificando se a prestação mensal ultrapassa 30% do salário.

# Solicita o valor do imóvel.
valor = float(input('Qual o valor do imovel que você pretende comprar?: R$'))

# Solicita o salário do comprador.
salario = float(input('Qual o seu salário?: R$'))

# Solicita o prazo de pagamento em anos.
anos = int(input('Quantos anos você pretende pagar?:'))

# Calcula o valor da prestação mensal.
# Multiplica os anos por 12 para obter o total de meses.
mensalidade = valor / (anos * 12)

# Exibe o valor do imóvel, o prazo e a prestação calculada.
print('Para pagar um imovel de R${:.2f} em {} anos a mensalidade será de {:.2f}'.format(valor,anos,mensalidade))

# Verifica se a prestação compromete até 30% do salário.
if mensalidade <= salario * 0.30:
    # Calcula e exibe o percentual do salário comprometido.
    print('A mensalidade compromete {:.2f}% do seu salário'.format(mensalidade / salario * 100))

    # Aprova o empréstimo.
    print('Emprestimo ACEITO!')
else:
    # Calcula e exibe o percentual do salário comprometido.
    print('A mensalidade compromete {:.2f}% do seu salário'.format(mensalidade / salario * 100))

    # Recusa o empréstimo.
    print('Emprestimo RECUSADO!')



