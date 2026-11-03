# Exercício 045 - Jogo de Jokenpô
# Simula uma partida de Pedra, Papel e Tesoura
# entre o jogador e o computador.

# Importa a função randint do módulo random.
from random import randint

# Cria uma tupla com as três jogadas possíveis.
itens = ('Pedra', 'Papel', 'Tesoura')

# Sorteia a jogada do computador (0, 1 ou 2).
computador = randint(0, 2)

# Apresenta as opções disponíveis para o jogador.
print('SUAS OPÇÕES')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')

# Solicita a jogada do usuário.
jogador = int(input('Qual a sua jogada?: '))

# Verifica se a opção escolhida é válida.
if jogador == 0 or jogador == 1 or jogador == 2:

    # Exibe as jogadas utilizando os índices da tupla.
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))

    # Verifica o resultado quando o computador escolhe Pedra.
    if computador == 0:
        if jogador == 0:
            resultado = 'EMPATE!'
        elif jogador == 1:
            resultado = 'JOGADOR VENCE'
        else:
            resultado = 'COMPUTADOR VENCE'

    # Verifica o resultado quando o computador escolhe Papel.
    elif computador == 1:
        if jogador == 0:
            resultado = 'COMPUTADOR VENCE'
        elif jogador == 1:
            resultado = 'EMPATE!'
        else:
            resultado = 'JOGADOR VENCE'

    # Verifica o resultado quando o computador escolhe Tesoura.
    elif computador == 2:
        if jogador == 0:
            resultado = 'JOGADOR VENCE'
        elif jogador == 1:
            resultado = 'COMPUTADOR VENCE'
        else:
            resultado = 'EMPATE!'

    # Exibe o resultado final da partida.
    print('RESULTADO: {}'.format(resultado))

# Informa quando o jogador escolhe uma opção inválida.
else:
    print('VALOR INVALIDO')

