import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumenta 10%, temos {moeda.aumenta(p, 10, True)}')
print(f'Reduz 13%, temos {moeda.diminui(p, 13, True)}')