lp= float(input('Largura da parede: '))
ap= float(input('Altura da parede: '))
print('Sua parede tem dimensão e {} x {} e sua área é de {:.2f}m²'.format(lp,ap,lp*ap))
print('Para pintar essa parede, você precisa de {:.2f}l de tinta'.format(lp*ap/2))
