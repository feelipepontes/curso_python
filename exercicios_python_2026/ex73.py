times = ('Palmeiras','Flamengo','Fluminense','Athletico-PR', 'Bragantino','Bahia','Coritiba',
         'São Paulo','Atlético-MG','Corinthians','Cruzeiro','Botafogo','Vitória','Internacional',
         'Santos','Grêmio','Vasco','Remo','Mirassol','Chapecoense')
primeiros = times[:5]
ultimos = times[-4:]
ordem = sorted(times)
chape = (times.index('Chapecoense')+1)
print('-='*15)
print(f'Lista de times do Brasileirão Serie A 2026: {times}')
print('-='*15)
print(f'Os 5 primeiros são: {primeiros}')
print('-='*15)
print(f'Os 4 ultimos são: {ultimos}')
print('-='*15)
print(f'Os times em ordem alfabetica: {ordem}')
print('-='*15)
print(f'A Chapecoense está na {chape}ª posição')