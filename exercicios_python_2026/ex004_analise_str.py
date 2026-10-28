# Exercício 004 - Análise de uma string
# Objetivo: identificar o tipo primitivo e verificar as características
# do conteúdo digitado pelo usuário.

a = input('Digite qualquer coisa: ')
print('O tipo primitivo desse valor é',type(a))
print('Só tem espaços?',a.isspace())
print('É um numero?',a.isnumeric())
print('É alfabetico?',a.isalpha())
print('é alfanumerico?',a.isalnum())
print('Maiusculo?',a.isupper())
print('Minusculo?',a.islower())
print('Esta capitalizada?',a.istitle())