# Exercício 010 - Conversão de reais para dólares
# Objetivo: receber um valor em reais (float) e calcular
# seu equivalente em dólares, utilizando uma cotação fixa.

n1 = float(input('Quanto de dinheiro você tem? R$: '))

# A cotação do dólar pode ser armazenada em uma variável
# ou utilizada diretamente na expressão matemática.
# Neste exercício, foi utilizada a cotação fixa de R$ 5,39 por US$ 1.
print('Com R${:.2f} você pode comprar US${:.2f}'.format(n1,n1/5.39))
