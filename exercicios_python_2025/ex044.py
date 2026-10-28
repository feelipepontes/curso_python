valor = float(input('Qual a valor do produto? R$: '))
print('Selecione a forma de pagamento: \n[1] à vista no dinheiro ou pix\n[2] à vista no cartão de debito\n[3] até 2x no cartão de crédito\n[4] em 3x ou mais no cartão de crédito')
pagamento = int(input('Pagamento: '))
if pagamento == 1:
    print('O pagamento a vista no dinheiro ou pix da 10% de desconto, o valor final da sua compra é de R${:.2f}'.format(valor - valor * 10/100 ))
elif pagamento == 2:
    print('O pagamento a vista no cartão de debito da 5% de desconto, o valor final da sua compra é de R${:.2f}'.format(valor - valor * 5/100))
elif pagamento == 3:
    print('O pagamento até 2x no cartão de crédito não recebe descontos e nem acrescimos, o valor final da sua compra é de R${:.2f}'.format(valor))
elif pagamento == 4:
    print('O pagamento em 3x ou mais no cartão de crédito recebe um acrescimo de 20%, o valor tinal da sua compra é de R${:.2f}'.format(valor + valor * 20/100))
