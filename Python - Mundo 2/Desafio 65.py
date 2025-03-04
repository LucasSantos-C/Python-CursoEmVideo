num = count = soma = maior = menor = 0
option = 'S'
while option == "S":
    num = int(input('Digite um número: '))
    soma += num
    count += 1
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
           maior = num
        if num < menor:
           menor = num
    option = str(input('Quer continuar? ')).upper().strip()
print(f'Voce digitou {count} números e a média é de: {soma / count:.1f}')
print(f'Maior:{maior} / Menor = {menor}')