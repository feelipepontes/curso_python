# Exercício 012 - Calculando descontos
# Calcula o novo preço de um produto após aplicar um desconto de 5%.

# Solicita o preço original do produto.
preço= float(input('Qual a valor do produto? R$: '))

# Calcula o valor correspondente a 5% do preço original.
desconto= preço*0.05

# Subtrai o desconto do preço original para obter o novo preço.
novopreço= preço-desconto

# Exibe o preço original e o preço após o desconto.
print('O produto que custava R${}, na promoção com 5% de desconto vai custar R${}'.format(preço,novopreço))


