# Exercício 024 - Verificando o início de uma string
# Verifica se o nome de uma cidade começa com a palavra "RIO".

# Solicita o nome da cidade e remove espaços no início e no final.
cidade = str(input('Em qual cidade você nasceu?: ')).strip()

# Converte o nome para maiúsculas e verifica se começa com "RIO".
# Retorna True se começar com "RIO" e False caso contrário.
print((cidade.upper().startswith('RIO')))


