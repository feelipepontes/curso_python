from random import randint ###Modulo que tem o randomizador
from time import sleep ###Modulo que faz o computado "esperar"
computador = randint (1,5) ###Pediu para o computador escolher um numero aleatorio
print('-=-' *20)
print('Pensei em um numero entre 1 a 5, tente adivinhar!')
print('-=-' *20)
jogador = int(input('qual numero eu pensei?'))
print('LOADING ...')
sleep(3) ### espera 3 segundos antes de prosseguir com o codigo
print('Pensei no numero {}'. format(computador))
if computador == jogador:
    print('PARABÉNS VOCÊ GANHOU)
else:
    print('Você falhou')

