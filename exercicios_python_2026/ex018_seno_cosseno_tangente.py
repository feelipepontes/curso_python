# Exercício 018 - Seno, cosseno e tangente
# Calcula o seno, cosseno e tangente de um ângulo informado em graus.

# Importa a biblioteca math para utilizar funções trigonométricas.
import math

# Solicita o valor de um ângulo em graus.
ang= float(input('Digite o ângulo que você deseja: '))

# Converte o ângulo de graus para radianos e calcula o seno.
seno = math.sin(math.radians(ang))

# Converte o ângulo de graus para radianos e calcula o cosseno.
cosseno = math.cos(math.radians(ang))

# Converte o ângulo de graus para radianos e calcula a tangente.
tangente = math.tan(math.radians(ang))

# Exibe os resultados com duas casas decimais.
print('O angulo de {}º tem o SENO de {:.2f}'.format(ang,seno))
print('O angulo de {}º tem o COSSENO de {:.2f}'.format(ang,cosseno))
print('O angulo de {}º tem a TANGENTE de {:.2f}'.format(ang,tangente))


