r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triangulo')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('As retas {:.1f} {:.1f} e {:.1f} e formam um triangulo Equilátero'.format(r1, r2, r3))
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('As retas foram {:.1f} {:.1f} e {:.1f} e formam um triangulo Escaleno'.format(r1, r2, r3))
    else:
        print('As retas {:.1f} {:.1f} e {:.1f} e formam um triangulo Isósceles'.format(r1, r2, r3))
else:
    print('As retas não podem formar um triangulo')

