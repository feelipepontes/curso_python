d = int(input('Por quantos dias você alugou o carro?'))
km = float(input('Quantos Km você andou com o carro?'))
total = (d*60)+(km*0.15)
print('Você alugou o carro por {} dias e andou {} km, portanto você deve pagar R${:.2f}'.format(d,km,total))
