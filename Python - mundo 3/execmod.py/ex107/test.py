import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumenta 10%,temos {moeda.aumenta(p, 10)}')
print(f'Reduz 13%, temos {moeda.diminui(p, 13)}')