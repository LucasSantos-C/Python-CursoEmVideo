print("============ Loja =============")
compra = float(input('Preço das compras: R$'))
print('''[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartao
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção: '))

if opcao == 1:
    print(f'O preco final com desconto de 10%: R${compra - (compra * 0.10):.2f}')
elif opcao == 2:
    print(f'O preco final com desconto de 5%: R${compra - (compra * 0.05):.2f}')
elif opcao == 3:
    total = compra
    parcelas = compra / 2
    print(f'Sua compra será pacelada em 2x de R${parcelas}')
elif opcao == 4:
    total = compra + (compra * 0.20)
    totparc = int(input('Quantas parcelas: '))
    parcelas = total / totparc
    print(f'Sua compra será pacelada em {totparc}x de R${parcelas:.2f}')
    print(f'Sua compra de R${compra} ficará: R${total}')
else:
    total = 0
    print('Digite algo válido!')