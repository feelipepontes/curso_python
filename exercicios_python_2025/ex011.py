n1 = float(input('Qual a altura dessa parede em metros(m)?'))
n2 = float(input('Qual a largura dessa parede em metros(m)?'))
area = n1*n2
print('A parede em questão possiu {:.1f}m² de area'.format(area))
print('Para realizar a pintura dessa parede vai ser preciso {:.1f} litros de tinta'.format(area/2))
