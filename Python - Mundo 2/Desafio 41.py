from datetime import date

ano = date.today().year
data = int(input('Digite seu ano de nascimento: '))
idade = ano - data

if idade <= 9:
    print('Categoria Mirim')
elif idade <= 14:
    print('Categoria Infantil')
elif idade <= 19:
    print('Categora Junior')
elif idade <= 25:
    print('Categora Sênior')
else:
    print('Cateriogia Master')