salário = float(input('Digite o salário a sofrer um aumento: R$'))

if salário <= 1250.0:
    print(f'O salário R$ {salário} sofrerá um aumento de 15%, será: R$ {(salário * 0.15) + salário:.2f}')
else:
    print(f'O salário R$ {salário} sofrerá um aumento de 10%, será: R$ {(salário * 0.10) + salário:.2f}')