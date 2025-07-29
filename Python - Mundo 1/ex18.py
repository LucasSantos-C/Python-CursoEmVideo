from math import sin, radians, cos, tan

angulo = float(input('Insira um angulo: '))

print(f'O seno de {angulo} é: {sin(radians(angulo)):.2f}')     
print(f'O cosseno de {angulo} é: {cos(radians(angulo)):.2f}')
print(f'O tangente de {angulo} é: {tan(radians(angulo)):.2f}')
