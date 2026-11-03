# Exercício 014 - Conversor de temperaturas
# Converte uma temperatura de graus Celsius para Fahrenheit.

# Solicita a temperatura em graus Celsius.
temp = float(input('Informe a temperatura em ºC: '))

# Converte a temperatura de Celsius para Fahrenheit.
# Fórmula: °F = (°C * 1.8) + 32
f = temp*1.8+32

# Exibe a temperatura original e o resultado da conversão.
print('A temperatura de {}ºC corresponde a {}ºF'.format(temp,f))

