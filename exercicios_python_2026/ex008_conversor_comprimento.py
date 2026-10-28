# Exercício 008 - Conversor de unidades de comprimento
# Objetivo: receber uma distância em metros (float)
# e convertê-la para outras unidades de comprimento.

d1 = float(input('Uma distancia em metros(m) '))
print('A medida de {}m corresponde a'.format(d1))
print('{:.3f}km\n{:.2f}hm\n{:.1f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(d1/1000,d1/100,d1/10,d1*10,d1*100,d1*1000))