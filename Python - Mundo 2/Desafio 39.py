data = int(input('Digite seu ano de nascimento: '))

if (2025 - data) < 18:
    print('Você ainda irá se alistar')
elif (2025 - data) == 18:
    print('Está na hora de se alistar')
else:
    print('Já passou da hora de se alistar')