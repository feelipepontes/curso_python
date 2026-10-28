from random import randint
computador = randint(0,10)
tentativas = 1
print('Sou o seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
palpite = int(input('Qual o seu palpite? '))
while palpite != computador:
    if palpite > computador:
        print('Menos ... Tente mais uma vez.')
        palpite = int(input('Qual o seu palpite? '))
    elif palpite < computador:
        print('Mais ... Tente mais uma vez.')
        palpite = int(input('Qual o seu palpite? '))
    tentativas += 1
print('Parabéns você acertou! o numero escolhido foi {} e você acertou com {} tentativas'.format(computador,tentativas))