def dobro(n=0):
    res = n*2
    return res

def metade(n=0):
    res = n/2
    return res

def aumenta(n=0, qtd=0):
    res = n + (n/100)*qtd
    return res

def diminui(n, qtd):
    res = n - (n/100)*qtd
    return res

def moeda(n=0, moeda = 'R$'):
    return f'{moeda}{n:>.2f}'.replace('.',',')