def maior(*valores):
    cout = maior = 0
    print('-='*25)
    for n in valores:
        print(f'{n}', end=" ")
        if cout == 0:
            maior = n
        elif n > maior:
            maior = n
        cout += 1
    print(f'Foram encontrados {cout} valores')
    print(f'O maior valor encontrado foi {maior}')
    print('-='*25)
 
maior(1,2,3,5,3)
maior(10,2,3,4,5)