def ficha(nm="<desconhecido>", gols=0):
    print(f"O jogador {nm} fez {gols} gols(s) no campeonato.")

print('-'*30)
nome = input('Nome do Jogador: ')
gol = input('Número de gols: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome,gol)
