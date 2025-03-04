num = count = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    count += 1
    soma += num
print(f'Total de números: {count}')
print(f'Soma de todos os valores: {soma}')
   