n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if n1 > n2:
    maior = n1
elif n2 > n1:
    maior = n2
else:
    maior = n1
print('Tirando {} e {}, a média do aluno é {:.1f}'.format(n1,n2,media))
if media >= 7:
    print('O aluno está APROVADO!')
elif 4 <= media < 7:
    nota =  7 * 2 - maior
    print('O aluno está de RECUPERAÇÃO, a nota {} foi mantida e ele precisa tirar {:.1f} para passar'.format(maior,nota))
    print('Pois ao tirar {} e somar com a sua maior nota {} ele atinge {} de média, ficando APROVADO!'.format(nota,maior,(nota+maior)/2))
else:
    print('O aluno está REPROVADO!')
