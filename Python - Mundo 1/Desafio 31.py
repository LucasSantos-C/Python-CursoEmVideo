pergunta = float(input('Digite a distancia da viagem me Km: '))

if pergunta < 200:
    print(f'O preco a ser pago abaixo de 200Km é de: R$ {pergunta * 0.50:.2f}')
else:
    print(f'O valor a ser pago acima de 200Km é de: R$ {pergunta * 0.45:.2f}')