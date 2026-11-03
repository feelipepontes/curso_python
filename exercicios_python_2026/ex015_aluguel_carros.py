# Exercício 015 - Aluguel de carros
# Calcula o valor total do aluguel de um carro com base
# na quantidade de dias alugados e nos quilômetros rodados.

# Solicita a quantidade de dias em que o carro foi alugado.
dia = int(input('Por quantos dias o carro foi alugado? '))

# Solicita a quantidade de quilômetros percorridos.
km = float(input('Quantos km foram rodados? '))

# Calcula o valor total considerando R$60 por dia e R$0,15 por km.
preço = (dia*60)+(km*0.15)

# Exibe o valor total a pagar com duas casas decimais.
print('O total a pagar é de R${:.2f}'.format(preço))


