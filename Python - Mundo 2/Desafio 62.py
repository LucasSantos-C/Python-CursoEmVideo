num = int(input('Primeiro termo: '))
r = int(input('Razao PA: '))
count = 1
total = 0
contagem = 10
while contagem !=0:
    total += contagem
    while count <= total:
        print(f'{num} -> ', end='')
        count +=1
        num += r
    print('PAUSA')
    contagem = int(input('Quantos termos voce quer a mais: '))
print(f'Termos mostrados: {total}')
   