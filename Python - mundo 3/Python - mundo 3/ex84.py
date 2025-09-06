dados = list()
lista = list()
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))    
    if len(dados) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    perg = input('Quer continuar? [S/N] ').upper()
    if perg == "N":
        break
print('-=-='*20)
print(f'Total de pessoas cadastradas: {len(lista)}')
print(f'Maior peso de {maior:.2f}kg. Peso de ', end="")
for p in lista:
    if p[1] == maior:
        print(f"[{p[0]}] ",end="")
print()
print(f'Menor peso: {menor:.2f}kg. Peso de ', end="")
for p in lista:
    if p[1] == menor:
        print(f"[{p[0]}] ",end="")
print()