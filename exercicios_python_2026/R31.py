d = float(input('Qual a distância da sua viagem em Km?: '))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('Sua viagem tem {:.1f}Km e vai custar R${:.2f}'.format(d, p))