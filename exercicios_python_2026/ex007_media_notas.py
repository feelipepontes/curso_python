# Exercício 007 - Média de duas notas
# Objetivo: receber duas notas do tipo float
# e calcular a média entre elas

n1= float(input('Primeira Nota '))
n2= float(input('Segunda Nota '))

# O :.1f formata a exibição de um número a uma casa decimal.
print('A média entre a {:.1f} e {:.1f} é {:.1f}'.format(n1,n2,(n1+n2)/2))
