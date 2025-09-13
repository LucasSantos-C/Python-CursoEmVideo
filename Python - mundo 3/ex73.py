times = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Internacional', 'Flamengo',
          'São Paulo', 'Cruzeiro', 'Bahia', 'Corinthians','Vitória', 'Vasco',
        'Juventude', 'Grêmio', 'Fluminense', 'Atlético-MG' , 'RB Bragantino', 
        'Santos', 'São Paulo','Sport','Vasco',)

print("-="*15)
print(f'Lista completa: {times}')
print("-="*15)
print(f'Primeiros 5 times: {times[:5]}')
print("-="*15)
print(f'Últimos 4 times: {times[-4:]}')
print("-="*15)
print(f'Lista em ordem alfabética: {sorted(times)}')
print("-="*15)
print(f'Chapecoense na {times.index("Chapecoense")+1} posicao')
