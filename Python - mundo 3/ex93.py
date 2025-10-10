jogador = dict()
gols = list()

jogador['nome'] = str(input("Nome do Jogador: "))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for i in range(0, partidas):
    gols.append(int(input(f"\tQuantos gols na partida {i}: ")))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
   
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O Campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partida.')
for i, v in enumerate(jogador['gols']):
    print(f'\t => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')