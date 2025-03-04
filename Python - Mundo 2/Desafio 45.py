from random import randint
from time import sleep

print('======== JO-KEN-PO =========')
print('''Suas opções:
[ 1 ]PEDRA      
[ 2 ]PAPEL     
[ 3 ]TESOURA ''')
jogada = int(input('Qual será sua jogada? '))
itens = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
computador = randint(1,3)
print('JO-KEN-PO...')
sleep(3)

if computador == jogada:
    print('-=-'*10)
    print('EMPATE!!')
    print('-=-'*10)
elif (computador == 1 and jogada == 2) or (computador == 2 and jogada == 3) or (computador == 3 and jogada == 1):
    print('-=-'*10)
    print('Você venceu!!!')
    print('-=-'*10)
elif (computador == 2 and jogada == 1) or (computador == 3 and jogada == 2) or (computador == 1 and jogada ==3):
    print('-=-'*10)
    print('Computador venceu!!!')
    print('-=-'*10)
else:
    print('Digite algo valido!!!')
print(f'Computador escoleu: {itens[computador]}')
print(f'Você escolheu: {itens[jogada]}')
print('-=-'*10)