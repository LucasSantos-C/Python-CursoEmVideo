valores = list()
impar = list()
par = list()

while True:
    i = int(input('Digite um valor: '))
    valores.append(i)
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
    perg = input('Quer continuar [S/N]: ').upper()
    if perg == 'N':
        break
  
print(f'Lista completa: {valores}')
print(f'Pares: {par}')
print(f'Impares: {impar}')