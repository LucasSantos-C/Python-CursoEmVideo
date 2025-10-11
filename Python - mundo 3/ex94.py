dados = dict()
pessoa = list()
soma = media = 0

while True:
    dados.clear()
    dados['nome'] = str(input("Nome: "))

    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoa.append(dados.copy())
    
    while True:
        escolha = input('Quer continuar? [S/N] ').upper()[0]
        if escolha in "SN":
            break
        print('ERRO! Responda apenas S ou N.')
    if escolha == 'N':
        break

print('-='*30)
print(f'A) Ao todo temos {len(pessoa)} pessoas cadastradas')
media = (soma/len(pessoa))
print(f'B) Media de idades: {media:5.2f}')

print(f'C) Mulheres cadastradas: ', end='')
for p in pessoa:
    if p['sexo'] == "F":
        print(f'{p["nome"]} ', end='')
    print()

print(f'D) Acima da media: ', end='')
for p in pessoa:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v};', end="")
        print()
print('<< ENCERRADO >>')

