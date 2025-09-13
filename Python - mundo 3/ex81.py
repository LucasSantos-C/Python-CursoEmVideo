valor = list()
while True:
    valor.append(int(input('Digite um numero: ')))
    perg = input('Quer continuar? [S/N] ').lower()
    if perg == 'n':
        break

print("=-=-="*30)
print(f'Quantidade de valor: {len(valor)}')
valor.sort(reverse=True)
print(f'Orderm decrescente: {valor}')

if 5 in valor:
    print('5 Faz parte da lista')
else:
    print('5 nao se encontra na lista')