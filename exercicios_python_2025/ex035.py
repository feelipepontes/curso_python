print('-=-' * 20)
print('Analisador de triangulos')
print('-=-' * 20)
r1 = float(input('Primeira reta mede quanto?'))
r2 = float(input('Segunda reta mede quanto?'))
r3 = float(input('Terceira reta mede quanto?'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os valores podem formar um triangulo')
else:
    print('Os valores não podem formar um triangulo')

