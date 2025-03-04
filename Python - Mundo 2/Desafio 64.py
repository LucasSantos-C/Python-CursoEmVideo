num = count = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    count += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print(f'Total de números digitados: {count }')
print(f'Total da soma: {soma}')

