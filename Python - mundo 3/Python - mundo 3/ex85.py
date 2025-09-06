valor = [[],[]]
dado = 0
for n in range(1,8):
    dado = (int(input(f'Digite o {n}º valor: ')))
    if n % 2 == 0:
        valor[0].append(dado)
    else:  
        valor[1].append(dado)

print("=-"*20)
valor[0].sort()
valor[1].sort()
print(f"Pares digitados: {valor[0]}")
print(f"Impares digitados: {valor[1]}")
