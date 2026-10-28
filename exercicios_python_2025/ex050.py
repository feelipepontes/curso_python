soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {} numero: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Você informou {} numeros pares e a soma foi {}'.format(cont,soma))
#### OU ####
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
# Verificação após o laço
if cont == 0:
    print("Nenhum número par foi digitado.")
else:
    print('Você informou {} números pares e a soma foi {}'.format(cont, soma))




