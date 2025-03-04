somaidade = 0
maisvelho = 0
nomevelho = ''
count = 0
for c in range (1,5):
    print(f'------- {c}º PESSOAS -------')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: ')) 
    sexo = input('Sexo (M/F): ').upper()
    somaidade += idade
    if c == 1 and sexo in 'M':
        maisvelho = idade
        nomevelho = nome
    if sexo in 'M' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        count +=1
print(f'A média de idades é de {somaidade / 4:.1f}')
print(f'O homem mais velho se chama {nomevelho} e possuí {maisvelho} anos')
print(f'Ao todo, temos {count} mulheres com menos de 20 anos.')