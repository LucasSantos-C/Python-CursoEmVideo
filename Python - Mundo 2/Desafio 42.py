a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if ((a + b) > c) and ((a + c) > b) and ((b + a) > c):
    print('Forma um triangulo ', end='')
    if a == b == c:
        print("Equilátero!")
    elif (a == b != c) or (c == b !=a) or (a == c != b) : 
        print('Isósceles!')
    elif (a != b !=c) or (c != b !=a) or (a != c != b):
        print('Escaleno!')
else:
    print('Não forma um triangulo')
