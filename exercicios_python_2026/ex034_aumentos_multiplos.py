# Exercício 034 - Aumentos múltiplos
# Calcula o reajuste salarial de um funcionário,
# aplicando percentuais diferentes conforme o salário.

# Solicita o salário atual do funcionário.
salário = float(input('Qual o seu salário? R$:'))

# Verifica se o salário é superior a R$ 1.250,00.
if salário > 1250:
    # Calcula o novo salário com aumento de 10%.
    novo = salário + (salário * 0.10)

    # Armazena o percentual de aumento aplicado.
    aumento = 10
else:
    # Calcula o novo salário com aumento de 15%.
    novo = salário + (salário * 0.15)

    # Armazena o percentual de aumento aplicado.
    aumento = 15

# Exibe o salário original, o percentual de aumento
# e o novo salário com duas casas decimais.
print('Seu salário é de {:.2f} e houve um aumento de {}%, agora seu salário é de {:.2f}'.format(salário,aumento,novo))

