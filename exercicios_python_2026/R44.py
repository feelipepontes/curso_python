preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista no dinheiro/pix')
print('[ 2 ] à vista no cartão de debito')
print('[ 3 ] 2x no cartão de crédito')
print('[ 4 ] 3x ou mais no cartão de crédito')
pagamento = int(input('Qual a sua forma de pagamento?: '))
if pagamento == 1 or pagamento == 2:
    print('PAGAMENTO A VISTA')
    if pagamento == 1:
        print('Suas compras de R${:.2f} à vista no dinheiro ou pix ganharam 10% de desconto, novo valor R${:.2f}'.format(preço,preço - preço * 0.10))
    elif pagamento == 2:
        print('Suas compras de R${:.2f} à vista no cartão de debito ganharam 5% de desconto, novo valor R${:.2f}'.format(preço, preço - preço * 0.05))
elif pagamento == 3 or pagamento == 4:
    print('PAGAMENTO PARCELADO')
    parcela = int(input('Quantas parcelas?: '))
    if pagamento == 3:
        if parcela == 1 or parcela == 2:
            print('Suas compras de R${:.2f} parceladas em {}x no cartão não recebem descontos'.format(preço,parcela))
            print('Você vai pagar {} parcela(s) de R${:.2f}'.format(parcela,preço / parcela))
        else:
            print('OPÇÃO INVALIDA!')
    elif pagamento == 4:
        print('Suas compras de R${:.2f} parceladas em {}x no cartão possuem aumento de 20% e juros'.format(preço,parcela))
        print('Você vai pagar {} parcelas de R${:.2f}, totalizando R${:.2f} ao final'.format(parcela,(preço * 0.2 + preço) / parcela, preço + (preço * 0.20)))
else:
    print('OPÇÃO INVALIDA!')