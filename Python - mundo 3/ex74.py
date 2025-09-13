from random import randint
maior = 0
menor = 1
n1 = (randint(0,5),randint(0,5),randint(0,5),randint(0,5),randint(0,5))

for i in range(len(n1)): 
    if n1[i] < menor:
        menor = n1[i]
    if n1[i] > maior:
        maior = n1[i]

print(f'Todos os números: {n1}')
print(f'maior: {maior}')
print(f'menor: {menor}')