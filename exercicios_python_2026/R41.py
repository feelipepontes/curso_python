from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    categoria = 'Mirin'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Junior'
elif idade <= 25:
    categoria = 'Senior'
else:
    categoria = 'Master'
print('Categoria do aluno: {}'.format(categoria))

