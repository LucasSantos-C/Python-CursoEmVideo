peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (metros): '))
imc = peso / (altura**2)

if imc < 18.5:
    print(f'Magreza: {imc:.1f}')
elif 18.5 <= imc < 25:
    print(f'Normal: {imc:.1f}')
elif 25 <= imc < 30:
    print(f'Sobrepeso: {imc:.1f}')
elif 30 <= imc < 40:
    print(f'Obesidade: {imc:.1f}')
else:
    print(f'Obesidade Grave: {imc:.1f}')