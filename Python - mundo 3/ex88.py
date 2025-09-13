from random import randint
from time import sleep
print('''--------------------------------
      JOGO DA MEGA SENA
--------------------------------''')

total = []
dados = []

n = int(input('Quantos jogos serao sorteados: '))
print()
for i in range(0,n):
    cont = 0
    while True:
        num = randint(1,60)
        if num not in total:
            total.append(num)
            cont += 1
        if cont >= 6:
            break
    total.sort()
    dados.append(total[:])
    total.clear()
print('-='*3, f'Sorteando {n} Jogos', '-='*3)
for i, l in enumerate(dados):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
