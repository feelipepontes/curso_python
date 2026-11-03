# Exercício 039 - Alistamento militar
# Calcula a idade de uma pessoa e verifica se ela ainda vai
# completar 18 anos, completa neste ano ou já passou dessa idade.

# Importa a classe date do módulo datetime.
from datetime import date

# Obtém automaticamente o ano atual do sistema.
ano = date.today().year

# Solicita o ano de nascimento do usuário.
nasc = int(input('Digite o seu ano de nascimento: '))

# Calcula a idade que a pessoa completa no ano atual.
idade = ano - nasc

# Verifica se a pessoa ainda não completou 18 anos no ano atual.
if idade < 18:
    # Exibe o ano de nascimento e a idade calculada.
    print('Quem nasceu em {} tem ou completa {} anos em {}'.format(nasc,idade,ano))

    # Calcula quantos anos faltam para completar 18 anos.
    print('Ainda faltam {} ano(s) para o seu alistamento'.format(18 - idade))

    # Calcula o ano em que a pessoa completará 18 anos.
    print('Seu alistamento será em {}'.format(18 - idade + ano))

# Verifica se a pessoa completa 18 anos no ano atual.
elif idade == 18:
    print('Quem nasceu em {} tem ou completa {} anos em {}'.format(nasc,idade,ano))
    print('Seu alistamento é esse ano')

# Executa este bloco caso a pessoa já tenha ultrapassado os 18 anos.
else:
    print('Quem nasceu em {} tem ou completa {} anos em {}'.format(nasc,idade,ano))

    # Calcula quantos anos se passaram desde o ano em que completou 18.
    print('Ja se passaram {} ano(s) do seu alistamento'.format(idade - 18))

    # Calcula o ano em que a pessoa completou 18 anos.
    print('Você deveria ter se alistado em {}'.format(nasc + 18))


