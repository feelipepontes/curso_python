# Exercício 040 - Média escolar
# Calcula a média de duas notas e determina a situação do aluno.
# Em caso de recuperação, calcula a nota necessária para aprovação,
# considerando que a maior nota será mantida.

# Solicita as duas notas do aluno.
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

# Calcula a média aritmética das duas notas.
media = (n1 + n2) / 2

# Identifica qual das duas notas é a maior.
if n1 > n2:
    maior = n1
elif n2 > n1:
    maior = n2
else:
    # Se as notas forem iguais, utiliza a primeira.
    maior = n1

# Exibe as notas e a média calculada com uma casa decimal.
print('Tirando {} e {}, a média do aluno é {:.1f}'.format(n1,n2,media))

# Verifica se o aluno atingiu a média mínima para aprovação.
if media >= 7:
    print('O aluno está APROVADO!')

# Verifica se a média está entre 4 (inclusive) e 7 (exclusive).
elif 4 <= media < 7:
    # Calcula a nota necessária para atingir média 7,
    # considerando a maior nota como uma das duas avaliações.
    nota =  7 * 2 - maior

    # Informa a situação de recuperação e a nota necessária.
    print('O aluno está de RECUPERAÇÃO, a nota {} foi mantida e ele precisa tirar {:.1f} para passar'.format(maior,nota))

    # Demonstra o cálculo da média após a recuperação.
    print('Pois ao tirar {} e somar com a sua maior nota {} ele atinge {} de média, ficando APROVADO!'.format(nota,maior,(nota+maior)/2))

# Caso a média seja inferior a 4, o aluno é reprovado.
else:
    print('O aluno está REPROVADO!')

