v = float(input('Digite uma velocidade em Km/h: '))
if v > 80:
    multa = (v - 80) * 7
    print('Você está acima da velocidade permitida, sua velocidade é {}\nVocê pagará uma multa de R${:.2f}'.format (v, multa))
else:
    print('Você está dentro da velocidade permitida')
