cont = ('zero','um','dois','tres','quatro','cinco',
        'seis','sete','oito','nove','dez',
        'onze','doze','treze','quatorze','quinze',
        'dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    while True:
        num = int(input('Digite um numero de 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('Numero invalido, tente novamente.')
    print(f'Você digitou o numero {cont[num]}')
    while True:
        resp = input('Deseja continuar? [S/N]: ').strip().upper()
        if resp in ('S','SI','SIM'):
            break
        elif resp in ('N','NAO','NÃO'):
            print('Programa encerrado')
            exit()
        else:
            print('Resposta Inválida, tente novamente.')




