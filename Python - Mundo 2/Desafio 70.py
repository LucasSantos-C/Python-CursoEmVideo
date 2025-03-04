print('==============================')
print('       LOJA DO ADRIANO        ')
print('==============================')
soma = count = barato = cont = 0 
nomebarato = ''
while True:
    produto = input('Nome do Produto: ')
    preco = int(input('Preço: R$'))
    soma += preco
    cont += 1
    if preco > 1000:
        count += 1   
    if cont == 1 or preco < barato:    
        barato = preco
        nomebarato = produto     
    opcao = input('Quer continuar [S/N]').upper().split()[0]
    if opcao == "N":
        break
print('=======================')
print(f'Total da compra: R${soma}')
print(f'Produtos acima de R$1000: {count:.2f}')
print(f'Nome mais barato: {nomebarato} e preco: {barato}')
print('=======================')