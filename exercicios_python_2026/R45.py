from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('SUAS OPÇÕES')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')
jogador = int(input('Qual a sua jogada?: '))
if jogador == 0 or jogador == 1 or jogador == 2:
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    if computador == 0:
        if jogador == 0:
            resultado = 'EMPATE!'
        elif jogador == 1:
            resultado = 'JOGADOR VENCE'
        else:
            resultado = 'COMPUTADOR VENCE'
    elif computador == 1:
        if jogador == 0:
            resultado = 'COMPUTADOR VENCE'
        elif jogador == 1:
            resultado = 'EMPATE!'
        else:
            resultado = 'JOGADOR VENCE'
    elif computador == 2:
        if jogador == 0:
            resultado = 'JOGADOR VENCE'
        elif jogador == 1:
            resultado = 'COMPUTADOR VENCE'
        else:
            resultado = 'EMPATE!'
    print('RESULTADO: {}'.format(resultado))
else:
    print('VALOR INVALIDO')
