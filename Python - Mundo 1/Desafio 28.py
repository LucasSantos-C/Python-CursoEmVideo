from random import randint
from time import sleep

n = randint(0,5)
print("~~~~~~"*13)
print('Vou sortear um número de 0 a 5. Tente adivinhar qual é o número...')
print("~~~~~~"*13)
r = (int(input("Digite um número aleatório entre 0 e 5: ")))
print('Processando...')
sleep(3)

if r == n:
    print('Acertou!!')
else:
    print('Voce perdeu!!')
    
print(f'O número sorteado era {n}')
