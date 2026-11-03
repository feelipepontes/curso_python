# Exercício 029 - Radar eletrônico
# Verifica se um veículo ultrapassou o limite de 80 km/h
# e calcula uma multa de R$7,00 por km/h excedido.

# Solicita a velocidade do veículo em km/h.
v = int(input('Qual a velocidade do seu  carro? Km/h: '))

# Calcula a diferença entre a velocidade informada e o limite de 80 km/h.
ve = v - 80

# Verifica se a velocidade está abaixo de 80 km/h.
if v < 80:
    # Exibe uma mensagem caso o veículo esteja abaixo do limite.
    print('Dentro do limite de velocidade, tenha um bom dia!')
else:
    # Informa que o veículo está acima do limite.
    print('Você está acima do limite de velocidade')

    # Calcula a multa multiplicando o excesso de velocidade por R$7,00.
    print('Sua multa é de R${:.2f}'.format(ve*7))
