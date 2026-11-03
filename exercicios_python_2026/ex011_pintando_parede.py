# Exercício 011 - Pintando uma parede
# Calcula a área de uma parede e a quantidade de tinta necessária para pintá-la.
# Considera que 1 litro de tinta é suficiente para pintar 2 m².

# Solicita a largura e a altura da parede em metros.
lp = float(input('Largura da parede: '))
ap = float(input('Altura da parede: '))

# Calcula a área multiplicando a largura pela altura.
# Exibe o resultado com duas casas decimais.
print('Sua parede tem dimensão e {} x {} e sua área é de {:.2f}m²'.format(lp,ap,lp*ap))

# Divide a área por 2 para calcular a quantidade de tinta em litros.
print('Para pintar essa parede, você precisa de {:.2f}l de tinta'.format(lp*ap/2))

