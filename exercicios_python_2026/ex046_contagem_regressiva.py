# Exercício 046 - Contagem regressiva
# Realiza uma contagem regressiva de 10 até 0,
# com uma pausa entre os números.

# Importa a função sleep do módulo time.
from time import sleep

# Executa a contagem de 10 até 0, diminuindo de 1 em 1.
for cont in range(10, -1, -1):

    # Exibe o número atual da contagem.
    print(cont)

    # Aguarda meio segundo antes da próxima execução.
    sleep(0.5)

# Exibe a mensagem após o término da contagem.
print('BUM! BUM! POOOW!')
