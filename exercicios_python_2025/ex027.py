nome = str(input('Digite seu nome completo: ')).strip().title()
print('Seu nome completo é {}'.format(nome))
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu ultimo nome é {}'.format(nome.split()[-1]))
