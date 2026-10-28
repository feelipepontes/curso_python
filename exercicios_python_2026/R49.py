n = int(input('Digite um numero de 1 a 10 para descobrir sua tabuada: '))
for c in range (1,11):
    print('{} x {:2} = {}'.format(n,c,n*c))