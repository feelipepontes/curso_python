# Exercício 031 - Custo da viagem
# Calcula o preço de uma passagem com base na distância percorrida,
# utilizando tarifas diferentes para viagens de até 200 km e acima disso.

# Solicita a distância da viagem em quilômetros.
d = float(input('Qual a distância da sua viagem em Km?: '))

# Verifica se a distância é menor ou igual a 200 km.
if d <= 200:
    # Calcula o preço utilizando a tarifa de R$0,50 por km.
    p = d * 0.5
else:
    # Calcula o preço utilizando a tarifa de R$0,45 por km.
    p = d * 0.45

# Exibe a distância da viagem e o preço calculado.
# {:.1f} apresenta uma casa decimal e {:.2f} apresenta duas.
print('Sua viagem tem {:.1f}Km e vai custar R${:.2f}'.format(d, p))
