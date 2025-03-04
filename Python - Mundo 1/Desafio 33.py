n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 =int(input('Digite mais um número: '))

#Verifica Menor
menor = n1 
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n1:
    menor = n3
    
#Verifica maior
maior = n2
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n2 and n3 > n1:
    maior = n3
    
print(f'Maior: {maior}')
print(f'Menor: {menor}')