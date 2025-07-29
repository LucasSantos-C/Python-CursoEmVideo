valores = []
maior = 0
menor = 1

for i in range (0,5):
    valor = int(input(f'Insira um valor na posicao {i}: '))
    valores.append(valor)
    if valores[i] > maior:
        maior = valores[i]
    if valores[i] < menor:
        menor = valores[i]

print('=-=-='*10)
print(f'lista de valores: {valores}') 
print(f'Maior valor: {maior} nas posições: {valores.index(maior)}')
print(f'Menor valor: {menor} nas posições: {valores.index(menor)}')