listagem = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetaas',22.30,'Livro',34.90)

print('_'*44)
print(f'{"LISTAGEM DE PRECOS":^44}')
print('_'*44)
for i in range(0,len(listagem),2):
    print(f'{listagem[i]:.<34}',end='')
    print(f'R${listagem[i+1]:7.2f}')
print('_'*44)