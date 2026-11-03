# Exercício 026 - Analisando uma frase
# Conta quantas vezes a letra "A" aparece em uma frase
# e identifica as posições da primeira e da última ocorrência.

# Solicita uma frase, remove espaços das extremidades
# e converte todas as letras para maiúsculas.
frase = str(input('Digite uma frase: ')).strip().upper()

# Conta quantas vezes a letra "A" aparece na frase.
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))

# Localiza a primeira ocorrência da letra "A".
# Soma 1 para apresentar a posição começando em 1, e não em 0.
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))

# Localiza a última ocorrência da letra "A".
# Soma 1 para apresentar a posição começando em 1, e não em 0.
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))


