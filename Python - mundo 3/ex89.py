medias = []
dados = []
med = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    medias.append(dados[:])
    dados.clear()
    perg = input('Quer continuar? [S/N] ').upper()
    if perg == "N":
        break
print("-="*30)
print("No. Nome         Media")
print("------------------------")
for i in medias:
    print(f'{medias.index(i)}  {i[0]}        {(i[1]+ i[2]) / 2}')
print("------------------------")
while True:
    pessoa = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if pessoa == 999:
        break
    else:
        print(f'Notas de {medias[pessoa][0]}: {medias[pessoa][1], medias[pessoa][2]}')
print('FIM')