from datetime import date
atual = date.today.year()
maior = 0
menor = 0

for c in range(1,8):
    pergunta = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    if (atual - pergunta) >= 18:
        maior += 1
    else:
        menor += 1
print(f'Total de MAIORES de idade: {maior}')
print(f'Total de MENORES de idade: {menor}')