n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))
print ('Os numeros digitados foram {} e {}'. format(n1, n2))
if n1 > n2:
    print('O primeiro valor {} é maior'.format(n1))
elif n1 < n2:
    print ('O segundo valor {} é maior'.format(n2))
elif n1 == n2:
    print ('Não existe valor maior, os dois são iguais')

