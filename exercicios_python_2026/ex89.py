ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-="-'*26)
for i, l in enumerate(ficha):
    print(f'{i:<4}{l[0]:<10}{l[2]:>8.1f}')
while True:
    print('-='*30)
    opc = int(input('Quer mostrar notas de qual aluno? (999 para parar) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
