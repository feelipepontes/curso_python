from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('[0] Pedra\n[1] Papel\n[2] Tesoura')
jogador = int(input('Qual a sua jogada?: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('=-=' * 20)
if jogador == 0:
    print('Você escolheu Pedra')
elif jogador == 1:
    print('Você escolheu Papel')
elif jogador == 2:
    print('Você escolheu Tesoura')
print('=-=' * 20)
sleep(1)
print('O computador escolheu {}'.format(itens[computador]))
print('=-=' * 20)
sleep(1)
if computador == 0 and jogador == 1:
    print('Papel ganha da pedra, o Jogador ganhou!')
elif computador == 0 and jogador == 2:
    print('Tesoura perde para a pedra, o computador ganhou')
elif computador == 0 and jogador == 0:
    print('Os dois escolheram pedra, a rodada termina empatada')
elif computador == 1 and jogador == 1:
    print('Os dois escolheram papel, a rodada termina empatada')
elif computador == 1 and jogador == 2:
    print('Tesoura ganha do papel, o jogador ganhou!')
elif computador == 1 and jogador == 0:
    print('Pedra perde para a papel, o computador ganhou')
elif computador == 2 and jogador == 1:
    print('Papel perde para a tesoura, o jogador perdeu!')
elif computador == 2 and jogador == 2:
    print('Os dois escolheram tesoura, a rodada termina empatada')
elif computador == 2 and jogador == 0:
    print('Pedra ganha da tesoura, o jogador ganhou!')
