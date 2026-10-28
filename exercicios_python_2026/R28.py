import random
computador = random.randint(0, 10)
numero = int(input('Advinhe o numero que o computador está pensando (De 1 a 10): '))
print('Pensei no numero: {}'.format(computador))
if computador == numero:
    print('Você ACERTOU!')
else:
    print('Eu ganhei, pensei no numero {} e você pensou no {}.'.format(computador, numero))


