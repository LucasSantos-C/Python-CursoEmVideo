print("=======================")
print("         ATM           ")
print("=======================")
valor = int(input('Valor do Saque: R$ '))
ced = 100
count = 0
while True:
    if valor >= ced:
        valor -= ced
        count += 1
    else:
        if count > 0:
            print(f'Total de {count} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        count = 0
        if valor == 0:
            break
print('FIM')