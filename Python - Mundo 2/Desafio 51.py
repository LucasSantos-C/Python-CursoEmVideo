print('''============================
    10 TERMOS DE UMA PA
============================''')

n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range(1, 11):
    print(f'{n1}', end=' > ')
    n1 += r
print('Acabou!!!')