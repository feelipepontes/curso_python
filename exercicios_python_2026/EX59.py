n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
final = False
while not final:
    print(' '*5+'[ 1 ] Somar')
    print(' '*5+'[ 2 ] Multiplicar')
    print(' '*5+'[ 3 ] Maior')
    print(' '*5+'[ 4 ] Novos números')
    print(' '*5+'[ 5 ] Sair do programa')
    opção = int(input('>>>>> Qual é a sua opção?: '))
    if opção == 1:
        print('A soma  de {} + {} é {}'.format(n1, n2, n1 + n2))
    elif opção == 2:
        print('A multiplicação de {} * {} é {}'.format(n1,n2,n1 * n2))
    elif opção == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1,n2,n1))
        elif n2 > n1:
            print('Entre {} e {} o maior valor é {}'.format(n1,n2,n2))
        else:
            print('Os numeros são iguais')
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        final = True
        print('Saindo do programa ...')
    else:
        print('Opção invalida, tente novamente')
