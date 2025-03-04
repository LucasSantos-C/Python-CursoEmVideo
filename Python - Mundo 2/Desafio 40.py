nota1 = float(input('Escreva a primeira nota: '))
nota2 = float(input('Escreva a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Reprovado: {media:.1f}')
elif 7 > media >= 5.0:
    print(f'Recuperação:  {media:.1f}')
elif media > 7:
    print(f'Aprovado: {media:.1f}')