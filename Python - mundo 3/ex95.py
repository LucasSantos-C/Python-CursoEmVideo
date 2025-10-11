jogador = dict()
players = list()
gols = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do Jogador: "))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    gols.clear()
    for i in range(0, partidas):
        gols.append(int(input(f"\tQuantos gols na partida {i+1}: ")))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    players.append(jogador.copy())
    while True:
        perg = input('Quer continuar? [S/N]').upper()[0]
        if perg in 'SN':
            break
    if perg == 'N':
        break
        
print('-='*30)
print('cod nome          gols      total')
print('--'*30)

for k,v in enumerate(players):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados do jogador com codigo (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(players):
        print(f'ERRO! Nao existe jogador com codigo {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADR {players[busca]["nome"]}:')
        for i,g in enumerate (players[busca]['gols']):
            print(f'     No jogo{i+1} fez {g} gols.')
    print('-='*30)
print('Tchau!!!!!')
