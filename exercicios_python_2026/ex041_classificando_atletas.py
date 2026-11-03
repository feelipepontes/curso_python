# Exercício 041 - Classificando atletas
# Calcula a idade de um atleta e determina sua categoria
# esportiva com base na faixa etária.

# Importa a classe date do módulo datetime.
from datetime import date

# Solicita o ano de nascimento do atleta.
nasc = int(input('Digite seu ano de nascimento: '))

# Obtém automaticamente o ano atual do sistema.
ano = date.today().year

# Calcula a idade que o atleta completa no ano atual.
idade = ano - nasc

# Exibe a idade calculada.
print('O atleta tem {} anos'.format(idade))

# Classifica atletas de até 9 anos na categoria Mirim.
if idade <= 9:
    categoria = 'Mirim'

# Classifica atletas de 10 a 14 anos na categoria Infantil.
elif idade <= 14:
    categoria = 'Infantil'

# Classifica atletas de 15 a 19 anos na categoria Junior.
elif idade <= 19:
    categoria = 'Júnior'

# Classifica atletas de 20 a 25 anos na categoria Senior.
elif idade <= 25:
    categoria = 'Sênior'

# Classifica atletas acima de 25 anos na categoria Master.
else:
    categoria = 'Master'

# Exibe a categoria correspondente à idade do atleta.
print('Categoria do aluno: {}'.format(categoria))


