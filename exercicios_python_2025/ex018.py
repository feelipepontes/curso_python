import math
a = float(input('Digite um angulo'))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O sen do angulo é {:.2f}\nO cos do angulo é {:.2f}\nA tan do angulo é {:.2f}'.format(sen,cos,tan))