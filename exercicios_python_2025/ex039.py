from datetime import datetime
nasc = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - nasc
if idade == 17:
    print ('Você ainda não está na idade para o alistamento militar obrigatorio, ainda falta 1 ano para o alistamento')
elif idade < 17:
    print('Você ainda não está na idade para o alistamento militar obrigatorio, ainda faltam {} anos para o alistamento'.format(18 - idade))
elif idade == 18:
    print ('Você está na idade do para o alistamento militar obrigatorio, vá ate a junta militar')
elif idade == 19:
    print('Você passou da idade para o alistamento militar obrigatorio. Você passou 1 ano do prazo, vá ate a junta militar')
else:
    print ('Você passou da idade para o alistamento militar obrigatorio. Você passou {} anos do prazo, vá ate a junta militar e regularize sua situação'.format(idade-18))
    