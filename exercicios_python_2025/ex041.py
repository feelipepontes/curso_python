from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('O atleta de {} anos pertence a categoria Mirim'.format(idade))
elif idade >= 10 and idade <= 14:
    print('O atleta de {} anos pertence a categoria Intantil'.format(idade))
elif idade >= 15 and idade <= 19:
    print('O atleta de {} anos pertence a categoria Junior'.format(idade))
elif idade == 20:
    print('O atleta de 20 anos pertence a categoria Sênior')
else:
    print('O atleta de {} anos pertence a categoria Master'.format(idade))
