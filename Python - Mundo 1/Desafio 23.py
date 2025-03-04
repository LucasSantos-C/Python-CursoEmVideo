n1 = int(input('Escreva um número inteiro: '))

print(f'Unidade: {n1 // 1 % 10}')
print(f'Dezena: {n1 // 10 % 10}')
print(f'Centena: {n1 // 100 % 10}')
print(f'Milhar: {n1 // 1000 % 10}')
