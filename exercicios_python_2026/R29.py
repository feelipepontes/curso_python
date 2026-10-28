v = int(input('Qual a velocidade do seu  carro? Km/h: '))
ve = v - 80
if v < 80:
    print('Dentro do limite de velocidade, tenha um bom dia!')
else:
    print('Você está acima do limite de velocidade')
    print('Sua multa é de R${:.2f}'.format(ve*7))