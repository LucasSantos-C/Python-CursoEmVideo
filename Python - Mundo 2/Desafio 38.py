n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'Maior: {n1}')
elif n1 < n2:
    print(f'Maior: {n2}')
else:
    print(f'Os valor {n1} e {n2} são iguais')