lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = (input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa é {lista}')
print(f'Os valores pares digitados foram {par}')
print(f'Os valores impares digitados foram {impar}')
