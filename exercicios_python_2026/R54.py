from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for c in range (1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu: '.format(c)))
    if anoatual - nasc >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))



