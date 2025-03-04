print('''----------------------
Sequencia de Fibonacci
----------------------''')
termo = int(input('Quantos termos serao mostrados: '))
num1 = 0
num2 = 1
count = 2
print(f'{num1} -> {num2} ', end='')
while count < termo:
    num3 = num1 + num2
    print(f'-> {num3} ', end='')
    count += 1 
    num1 = num2
    num2 = num3
print('-> Fim', end='')
