nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 8:
    print('Sua média foi {}. Você está APROVADO'.format(media))
elif media >=5 and media < 7.9:
    print('Sua média foi {}. Você está de RECUPERAÇÃO'.format(media))
else:
    print('Sua média foi {}. Você está REPROVADO'.format(media))
