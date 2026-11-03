# Exercício 028 - Jogo da adivinhação
# Sorteia um número aleatório e verifica se o usuário
# conseguiu adivinhar o número escolhido pelo computador.

# Importa a biblioteca random para gerar números aleatórios.
import random

# Sorteia um número inteiro entre 0 e 10, incluindo os extremos.
computador = random.randint(0, 10)

# Solicita ao usuário um número para tentar adivinhar o sorteado.
numero = int(input('Advinhe o numero que o computador está pensando (De 0 a 10): '))

# Exibe o número escolhido pelo computador.
print('Pensei no numero: {}'.format(computador))

# Verifica se o número informado é igual ao número sorteado.
if computador == numero:
    # Executa este bloco caso os números sejam iguais.
    print('Você ACERTOU!')
else:
    # Executa este bloco caso os números sejam diferentes.
    print('Eu ganhei, pensei no numero {} e você pensou no {}.'.format(computador, numero))



