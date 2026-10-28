salário = float(input('Qual o seu salário? R$:'))
if salário > 1250:
    novo = salário + (salário * 0.10)
    aumento = 10
else:
    novo = salário + (salário * 0.15)
    aumento = 15
print('Seu salário é de {:.2f} e houve um aumento de {}%, agora seu salário é de {:.2f}'.format(salário,aumento,novo))
