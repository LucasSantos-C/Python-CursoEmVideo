from random import randint
count = 0

print('''============================
        PAR OU IMPAR
============================ ''')
while True:
    num = int(input('Diga um valor: '))
    computador = randint(0,10)
    soma = num + computador
    escolha = ''
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar [P/I]: ')).upper().strip([0])
    print(f'Voce escolheu: {num}. Computador escolheu: {computador}. Total ficou: {soma}')
    if escolha == 'P':
        if soma % 2 == 0:
            print('VOCE VENCEU!!')
            count += 1
        else:
            break 
    elif escolha == 'I':
        if soma % 2 == 1:
            print('VOCE VENCEU')
            count += 1
        else:
            break 
    print('Vamos jogar novamente...')  
print(f'Voce perdeu. Vitórias consecutivas: {count} ')
