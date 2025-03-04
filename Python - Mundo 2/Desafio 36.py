casa = float(input('Qual o Valor da casa: '))
salário = float(input('Qual o valor de seu salário: '))
anos = int(input('Quantos anos você irá pagar: '))

prestacao = casa / (anos * 12)
print(prestacao)

if prestacao <= (salário * 0.30):
    print('Empréstimo negado')
else:
    print(f'Você irá parar: R${prestacao:.2f} de prestações mensais')