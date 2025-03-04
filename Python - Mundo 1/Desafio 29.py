velocidade = float(input('Escreva a velocidade do carro: '))

if velocidade <= 80:
    print('Sua velocidade está normal. Dirija com seguranca!')
else:
    print(f'Velocidade limite ultrapassada! Pagar R$ {(velocidade - 80) * 7.00:.2f} em multa! ')