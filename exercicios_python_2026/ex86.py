valores = [[],[],[]]
for c in range(0,3):
    linha1 = int(input(f'Digite um valor para [0,{c}]: '))
    valores[0].append(linha1)
for c in range(0, 3):
    linha2 = int(input(f'Digite um valor para [1,{c}]: '))
    valores[1].append(linha2)
for c in range(0, 3):
    linha3 = int(input(f'Digite um valor para [2,{c}]: '))
    valores[2].append(linha3)
print(valores[0])
print(valores[1])
print(valores[2])



