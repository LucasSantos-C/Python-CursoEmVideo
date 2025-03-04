while True:
    count = num = 0
    num = int(input('Digite um número para saber sua tabuada: '))
    print("=================="*2)
    if num < 0:
        break
    while count < 10:
        count += 1  
        print(f'{num} x {count} = {num*count}')
    print("=================="*2)
print('Tabuada encerada!')