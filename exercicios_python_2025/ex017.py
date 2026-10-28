import math
co = float(input('Digite o cateto oposto do triangulo'))
ca = float(input('Digite o cateto adjacente do triangulo'))
hp = math.hypot(co,ca)
print('A hipotenusa do triangulo é {:.2f}'.format(hp))
