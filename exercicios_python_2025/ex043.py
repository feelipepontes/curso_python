peso = float(input('Qual o seu peso?: '))
altura = float(input('Qual a sua altura?: '))
IMC = peso / altura ** 2
print('Seu IMC é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso!')
elif IMC < 25:
    print('Seu peso está normal!')
elif IMC < 30:
    print('Você está com sobre peso!')
elif IMC < 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade morbida!')
min = 18.5 * altura ** 2
max = 25 * altura ** 2
print('Para seu peso ser considerado normal ele deve estar entre {:.2f}Kg e {:.2f}Kg'.format(min, max))

