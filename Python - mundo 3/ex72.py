n2 = ('Zero', 'Um','Dois','Três','Quatro','Cinco','Seis',
      'Sete','Oito','Nove','Dez','Onze','Doze','Treze',
      'Quatorze','Quinze', 'Dezesseis','Dezessete','Dezoito',
      'Dezenove','Vinte')

while True:
    i = int(input('Insira um número entre 0 e 20: '))
    if i <= 20 or i >= 0:
        print(f"Seu número digitado foi: {n2[i]}")
        perg = input('Quer continuar? ').lower().strip()
        if perg[0] == "n": 
            break
    else:
        print('Tente novamente.',end="")
