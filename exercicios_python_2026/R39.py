from datetime import date
ano = date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = ano - nasc
if idade < 18:
    print('Quem nasceu em {} tem ou completa {} anos em {}'.format(nasc,idade,ano))
    print('Ainda faltam {} ano(s) para o seu alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'.format(18 - idade + ano))
elif idade == 18:
    print('Quem nasceu em {} tem ou completa {} anos em {}'.format(nasc,idade,ano))
    print('Seu alistamento é esse ano')
else:
    print('Quem nasceu em {} tem ou completa {} anos em {}'.format(nasc,idade,ano))
    print('Ja se passaram {} ano(s) do seu alistamento'.format(idade - 18))
    print('Você deveria ter se alistado em {}'.format(nasc + 18))

