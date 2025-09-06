valor = list()
perg = " "
while True:
    v = int(input('Digite um valor: '))
    if v in valor:
        print('Valor duplicado! Não vou adicionar..')
    else:
        valor.append(v)
        print('Valor adicionado com sucesso...')
    perg = input('Quer continuar? [S/N] ').lower().strip()
    if perg[0] == "n":
        break
print('=-=-='*10)
valor.sort()
print(f'Valores digitados: {valor}')