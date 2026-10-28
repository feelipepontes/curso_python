sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('Dado inválido, informe seu sexo corretamente')
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
if sexo == 'M':
    genero = 'Masculino'
elif sexo == 'F':
    genero = 'Feminino'
print('Sexo ({}) {} registrado com sucesso'.format(sexo,genero))