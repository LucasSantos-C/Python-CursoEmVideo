count = homem = menormulher = 0
while True:
    print("---------------------------")
    print('    Cadastre um Pessoa'     )
    print("---------------------------")
    idade = int(input('Idade: '))
    if idade > 18:
        count += 1
    sexo = str(input('Sexo [M/F]:')).upper()
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade < 20:
        menormulher += 1
    print("---------------------------")
    p = str(input('Quer continuar? ')).upper()
    if p == "N":
        break
print('======================================================')
print(f'Pessoas com mais de 18 anos: {count}')
print(f'Total de homens: {homem}')
print(f'Total de mulheres menores de 20 anos: {menormulher}')
print('======================================================')
