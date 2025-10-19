from random import randint
from time import sleep

def somaPar(vetor):
    soma = 0
    for n in vetor:
        if n % 2 == 0:
            soma += n
    print(f"somando os pares de {vetor}, temos {soma}")

def sorteia(vetor):
    print("Sorteando 5 valores da lista: ",end="")
    for i in range(0, 5):
        a = randint(1,10)
        vetor.append(a)
        print(f"{a} ", end="", flush=True)
        sleep(0.5)
    print("Pronto!")


vetor = []
sorteia(vetor)
somaPar(vetor)

