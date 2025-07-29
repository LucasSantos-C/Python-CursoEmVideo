d = int(input('Por quantos dia foi alugado:  '))
q = float(input('Quantos KM foram percorridos pelo carro alugado: '))
print(f'O preco a se pagar é: R${((d*60) + (q * 0.15)):.2f}')