def dobro(n=0, formato=False):
    res = n*2
    return res if not formato else moeda(res)

def metade(n=0, formato=False):
    res = n/2
    return res if not formato else moeda(res)

def aumenta(n=0, qtd=0, formato=False):
    res = n + (n/100)*qtd
    return res if not formato else moeda(res)

def diminui(n, qtd, formato=False):
    res = n - (n/100)*qtd
    return res if not formato else moeda(res)

def moeda(n=0, moeda = 'R$'):
    return f'{moeda}{n:>.2f}'.replace('.',',')