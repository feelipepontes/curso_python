# Exercício 032 - Ano bissexto
# Verifica se um ano é bissexto utilizando as regras
# de divisibilidade por 4, 100 e 400.

# Solicita ao usuário o ano que deseja analisar.
ano = int(input('Qual ano você quer analisar?: '))

# Verifica se o ano é divisível por 4 e não por 100,
# ou se é divisível por 400.
if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0:
    # Executa este bloco caso o ano seja bissexto.
    print('O ano {} é bissexto'.format(ano))
else:
    # Executa este bloco caso o ano não seja bissexto.
    print('O ano {} não é bissexto'.format(ano))

