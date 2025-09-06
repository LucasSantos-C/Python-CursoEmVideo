soma = spar = maior = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Digite o valor de [{i},{j}]: '))
print('=-'*25)
for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]:^5}]", end="")
        if matriz[i][j] % 2 == 0:
            spar += matriz[i][j]
    print()
print('=-'*25)

print(f'Soma dos pares: {spar}')
for i in range(0,3):
    soma += matriz[i][2]
print(f'Soma dos valores da 3º coluna: {soma}')

for j in range(0,3):
    if j == 0:
        maior = matriz[1][j] 
    elif matriz[1][j] > maior:
        maior = matriz[1][j]
print(f"Maior da 2º linha: {maior}")