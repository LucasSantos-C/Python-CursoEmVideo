from time import sleep

def contador (i,f,p):
    print('-='*20)
    print(f"Contagem de {i} até {f} de {p} em {p}")
    sleep(2)

    if p < 0:
        p *= -1
    
    if p == 0:
        p = 1

    if i < f:
        count = i
        while count <= f:
            print(f'{count}..', end=' ', flush=True)
            sleep(0.5)
            count += p
            sleep(1)
        print("FIM!!")
    else:
        count = i
        while count >= f:
            print(f'{count}..', end=' ', flush=True)
            sleep(0.5)
            count -= p
            sleep(1)
        print("FIM!!")
    print('-='*20)

contador(1, 10, 1)
contador(10, 1, 2)

print('Escreva uma contagem personalizada: ')
ini = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))
pas = int(input("Digite o passo: "))


contador(ini, fim, pas)
