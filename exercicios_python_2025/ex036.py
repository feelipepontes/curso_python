casa = float(input('Digite o valor da casa R$: '))
salário = float(input('Digite o seu salário R$: '))
anos = int(input('Em quantos anos você pretente pagar o emprestimo?: '))
prestação = casa / (anos * 12)
percentual = prestação / salário * 100
print('Para pegar uma casa de R${:.2f} em {} anos o valor da prestação será de R${:.2f}'.format(casa,anos,prestação))
if percentual > 30:
    print('Seu emprestimo não pode comprometer mais de 30% do seu salário, sua simulação compromete {:.2f}% do seu salário'.format(percentual))
    print('Seu emprestimo foi negado!')
else:
    print('Seu emprestimo não pode comprometer mais de 30% do seu salário, sua simulação compromete {:.2f}% do seu salário'.format(percentual))
    print('Seu emprestimo foi aprovado!')
