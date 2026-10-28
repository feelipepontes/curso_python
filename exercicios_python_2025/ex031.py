distância = float(input('Qual a distancia do seu destino em Km?: '))
if distância <= 200:
    preço = (distância * 0.50)
    print('Devido a distância de {}Km o valor da sua viagem é de R${:.2f}'.format(distância, preço))
else:
    print('Devido a distância de {}Km o valor da sua viagem é de R${:.2f}'.format(distância, distância*0.45))


