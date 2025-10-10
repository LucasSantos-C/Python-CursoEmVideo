from datetime import datetime

trabalho = dict()

trabalho['nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
trabalho['idade'] = datetime.now().year - nasc
trabalho['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalho['ctps'] != 0:
    trabalho['cont'] = int(input('Ano de Contratação: '))
    trabalho['salario'] = float(input('Salário: R$'))
    trabalho['aposentadoria'] = trabalho['idade'] + ((trabalho['cont'] + 35) - datetime.now().year)
print('-='*30)
for k,v in trabalho.items():
    print(f'\t- {k} tem o valor {v}')
