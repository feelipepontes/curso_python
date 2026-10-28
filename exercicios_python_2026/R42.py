n1 = float(input('Primeira reta: '))
n2 = float(input('Segunda reta: '))
n3 = float(input('Terceira reta: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('As retas podem formar um triangulo!')
    if n1 == n2 == n3:
        triangulo = 'equilatero'
    elif n1 == n2 or n1 == n3 or n2 == n3:
        triangulo = 'isosceles'
    else:
        triangulo = 'escaleno'
    print('As retas formam um triangulo {}'.format(triangulo))
else:
    print('As retas não podem formar um triangulo!')


