n = (int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')))

print(f'Valores digitados: {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')

if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1}º posicao')
else:
    print(f'O valor 3 apareceu nao está aqui')

print(f'Os valores pares digitados foram: ', end='')
for n in n: 
    if n % 2 == 0:
        print(n, end=' ')


