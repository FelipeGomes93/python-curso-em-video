'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Os 5 primeiros times;
B) Os últimos 4 colocados;
C) Tims em ordem alfabética;
D) Em que posição está o time da Chapecoense'''

times = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia', 'Corinthians', 'Athletico', 'Bragantino', 'Chapecoense', 'Mirassol', 'Coritiba', 'Flamengo', 'Botafogo', 'Grêmio', 'Vitória', 'Atlético MG', 'Remo', 'Vasco', 'Santos', 'Internacional', 'Cruzeiro')

print('-='*15)
print(f'Lista de times: {times}')
print('-='*15)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'A Chapecoense está na {times.index('Chapecoense')+1}ª posição')