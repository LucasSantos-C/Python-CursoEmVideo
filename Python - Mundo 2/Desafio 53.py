frase = input('Digite uma frase: ').strip().upper()
f1 = ''.join(frase.split())
inverso = ''

#Solucao sem FOR IN:
'''pali = (f1.upper()[::-1]).strip().upper()

#print(f'A frase {f1} ao inverso fica: {pali}')

#Solucao sem repeticao FOR IN:
if f1 == pali:
    print('Temos um PALÍNDROMO')
else:
    print('Não temos um PALÍNDROMO!')'''
    
#Solucao com FOR IN:
for c in range (len(f1)-1,-1,-1):
     inverso += f1[c]
print(inverso)
if f1 == inverso:
     print('Temos um PALÍNDROMO')
else:
    print('Não temos um PALÍNDROMO!')
 