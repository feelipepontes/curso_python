print('Todos os numeros pares no intervalo de 1 a 50')
for numero in range(2,51,2):
    if numero == 50:
        print(numero, end='.')
    else:
        print(numero, end=',')


