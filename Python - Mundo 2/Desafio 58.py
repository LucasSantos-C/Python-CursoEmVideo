from random import randint
from time import sleep
palpite = 0
r = 0

n = randint(0,10)
print("~~~~~~"*13)
print('Vou sortear um número de 0 a 5. Tente adivinhar qual é o número...')
print("~~~~~~"*13)

while r != n:
   r = (int(input("Digite um número aleatório entre 0 e 5: ")))
   print('Processando...')
   sleep(1)
   if r > n:
       palpite +=1
       print('um pouco menos!')
   if r < n:
       palpite += 1
       print('Um pouco mais!')
print("~~~~~~"*13)
palpite +=1       
print('Acertou!!!')
print(f'Número sorteado: {n} ')
print(f'Total de Palpites: {palpite} ')
print("~~~~~~"*13)
