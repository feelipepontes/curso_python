# Exercício 025 - Procurando uma string dentro de outra
# Verifica se o nome completo contém a sequência "SANTOS",
# independentemente de letras maiúsculas ou minúsculas.

# Solicita o nome completo e remove espaços no início e no final.
nome = str(input('Qual o seu nome completo?: ')).strip()

# Converte o nome para maiúsculas e verifica se contém "SANTOS".
# O operador 'in' retorna True se encontrar a sequência e False caso contrário.
print('Seu nome tem "Santos"? {}'.format('SANTOS' in nome.upper()))

