# Exercício 037 - Conversor de bases numéricas
# Converte um número inteiro para binário, octal ou hexadecimal,
# conforme a opção selecionada pelo usuário.

# Solicita um número inteiro para realizar a conversão.
n = int(input('Digite um numero inteiro: '))

# Exibe um menu com as três bases numéricas disponíveis.
# As aspas triplas permitem escrever o texto em várias linhas.
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

# Solicita a opção de conversão desejada.
opção = int(input('Sua Opção: '))

# Verifica se o usuário escolheu a conversão para binário.
if opção == 1:
    # Converte para binário e remove o prefixo "0b".
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))

# Verifica se o usuário escolheu a conversão para octal.
elif opção == 2:
    # Converte para octal e remove o prefixo "0o".
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))

# Verifica se o usuário escolheu a conversão para hexadecimal.
elif opção == 3:
    # Converte para hexadecimal e remove o prefixo "0x".
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))

# Executa este bloco caso nenhuma das opções anteriores seja selecionada.
else:
    print('Opção inválida. Selecione uma das 3 opções!')

