valor = float(input('Qual o valor do imovel que você pretende comprar?: R$'))
salario = float(input('Qual o seu salário?: R$'))
anos = int(input('Quantos anos você pretende pagar?:'))
mensalidade = valor / (anos * 12)
print('Para pagar um imovel de R${:.2f} em {} anos a mensalidade será de {:.2f}'.format(valor,anos,mensalidade))
if mensalidade <= salario * 0.30:
    print('A mensalidade compromete {:.2f}% do seu salário'.format(mensalidade / salario * 100))
    print('Emprestimo ACEITO!')
else:
    print('A mensalidade compromete {:.2f}% do seu salário'.format(mensalidade / salario * 100))
    print('Emprestimo RECUSADO!')


