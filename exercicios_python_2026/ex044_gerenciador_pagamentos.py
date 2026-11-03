# Exercício 044 - Gerenciador de pagamentos
# Simula diferentes formas de pagamento, aplicando descontos
# ou acréscimos conforme a opção escolhida pelo cliente.

# Solicita o valor total das compras.
preço = float(input('Preço das compras: R$'))

# Apresenta as formas de pagamento disponíveis.
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista no dinheiro/pix')
print('[ 2 ] à vista no cartão de debito')
print('[ 3 ] 2x no cartão de crédito')
print('[ 4 ] 3x ou mais no cartão de crédito')

# Solicita a opção de pagamento.
pagamento = int(input('Qual a sua forma de pagamento?: '))

# Verifica se o pagamento será à vista.
if pagamento == 1 or pagamento == 2:
    print('PAGAMENTO A VISTA')

    # Aplica desconto de 10% para dinheiro ou Pix.
    if pagamento == 1:
        print('Suas compras de R${:.2f} à vista no dinheiro ou pix ganharam 10% de desconto, novo valor R${:.2f}'.format(preço,preço - preço * 0.10))

    # Aplica desconto de 5% para cartão de débito.
    elif pagamento == 2:
        print('Suas compras de R${:.2f} à vista no cartão de debito ganharam 5% de desconto, novo valor R${:.2f}'.format(preço, preço - preço * 0.05))

# Verifica se o pagamento será parcelado.
elif pagamento == 3 or pagamento == 4:
    print('PAGAMENTO PARCELADO')

    # Solicita a quantidade de parcelas.
    parcela = int(input('Quantas parcelas?: '))

    # Trata o pagamento no cartão sem acréscimo.
    if pagamento == 3:

        # Aceita uma ou duas parcelas.
        if parcela == 1 or parcela == 2:
            print('Suas compras de R${:.2f} parceladas em {}x no cartão não recebem descontos'.format(preço,parcela))
            print('Você vai pagar {} parcela(s) de R${:.2f}'.format(parcela,preço / parcela))

        # Rejeita outras quantidades de parcelas nessa opção.
        else:
            print('OPÇÃO INVALIDA!')

    # Trata o pagamento com acréscimo de 20%.
    elif pagamento == 4:
        print('Suas compras de R${:.2f} parceladas em {}x no cartão possuem aumento de 20% e juros'.format(preço,parcela))

        # Calcula o total acrescido de 20% e divide pelas parcelas.
        print('Você vai pagar {} parcelas de R${:.2f}, totalizando R${:.2f} ao final'.format(parcela,(preço * 0.2 + preço) / parcela, preço + (preço * 0.20)))

# Rejeita formas de pagamento não cadastradas.
else:
    print('OPÇÃO INVALIDA!')
