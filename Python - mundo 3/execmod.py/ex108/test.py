import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumenta 10%,temos {moeda.moeda(moeda.aumenta(p, 10))}')
print(f'Reduz 13%, temos {moeda.moeda(moeda.diminui(p, 13))}')