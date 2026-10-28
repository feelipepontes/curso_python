aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input(f'Qual a média de {aluno["nome"]}? '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é {v}')
