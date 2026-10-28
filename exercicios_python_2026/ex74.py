from random import randint
numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Os valores sorteados foram {numeros}')
print(f'O maior valor sorteado foi o {max(numeros)}')
print(f'O menor valor sorteado foi o {min(numeros)}')