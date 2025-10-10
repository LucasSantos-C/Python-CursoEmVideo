aluno = dict()

aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média do aluno: '))

print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')

if aluno['media'] >= 6.00:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')
print()
