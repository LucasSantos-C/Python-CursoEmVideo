from math import hypot

co = float(input('Qual é a medida do cateto oposto: '))
ca = float(input('Qual é a medida do cateto adjacente: '))

print(f'a hipotenusa é: {hypot(co, ca):.2f}')