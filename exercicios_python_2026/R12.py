preço= float(input('Qual a valor do produto? R$: '))
desconto= preço*0.05
novopreço= preço-desconto
print('O produto que custava R${}, na promoção com 5% de desconto vai custar R${}'.format(preço,novopreço))

