# Exercício 043 - Índice de Massa Corporal (IMC)
# Calcula o IMC a partir do peso e da altura
# e classifica o resultado conforme as faixas estabelecidas.

# Solicita o peso da pessoa em quilogramas.
peso = float(input('Qual o seu peso? (Kg):'))

# Solicita a altura da pessoa em metros.
altura = float(input('Qual a sua altura? (m):'))

# Calcula o IMC dividindo o peso pela altura ao quadrado.
imc = peso / (altura ** 2)

# Verifica em qual faixa de IMC o resultado se encontra.
if imc < 18.5:
    resultado = 'Abaixo do peso'
elif imc < 25:
    resultado = 'Peso ideal'
elif imc < 30:
    resultado = 'Sobrepeso'
elif imc < 40:
    resultado = 'Obesidade'
else:
    resultado = 'Obesidade morbida'

# Exibe o IMC calculado com uma casa decimal.
print('Seu IMC é de {:.1f}'.format(imc))

# Exibe a classificação correspondente ao IMC.
print('Você está em {}'.format(resultado))

