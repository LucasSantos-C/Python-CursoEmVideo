a = float(input('Escreva uma reta: '))
b = float(input('Escreva outra reta: '))
c = float(input('Escreva mais uma reta: '))

if ((a + b) > c) and ((a + c) > b) and ((b + a) > c):
    print('É um triangulo')
else:
    print('Não é um triangulo')