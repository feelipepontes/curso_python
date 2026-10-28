peso = float(input('Qual o seu peso? (Kg):'))
altura = float(input('Qual a sua altura? (m):'))
imc = peso / (altura ** 2)
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
print('Seu IMC é de {:.1f}'.format(imc))
print('Você está em {}'.format(resultado))
