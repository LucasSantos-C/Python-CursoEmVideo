s = 0
for c in range(0, 6):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        s += n
    else:
        print('Valor Ignorado!!')    
print(f'A soma dos pares ficou: {s}')
