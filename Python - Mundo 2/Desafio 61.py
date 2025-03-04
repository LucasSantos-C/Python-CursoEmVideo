n1 = int(input('Digite um número: '))
r = int(input('Digite a razao da PA: '))
limite = 1

while limite <= 10:
    print(f'{n1} -> ', end='')
    n1 += r
    limite += 1 
print('FIM!!', end='')