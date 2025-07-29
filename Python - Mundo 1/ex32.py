from datetime import date

ano = int(input('Escreva um ano qualquer. Digite 0 para ver o ano do seu computador: '))

if ano == 0:
    ano == date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É Bissexto')
else:
    print('Não é Bissexto')