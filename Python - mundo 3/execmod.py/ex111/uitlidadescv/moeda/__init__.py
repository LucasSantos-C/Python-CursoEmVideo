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

def resumo(n, qtdmais=10, qtdmenos=5):
    print('_'*30)
    print('RESUMO DO VALOR'.center(30))
    print('_'*30)
    print(f"Preço analisado:    {moeda(n)}")
    print(f"Dobro do preço:     {dobro(n,True)}")
    print(f"Metade do preço:    {metade(n,True)}")
    print(f"{qtdmais}% de aumento:     {aumenta(n, qtdmais, formato=True)}")
    print(f"{qtdmenos}% de redução:      {diminui(n, qtdmenos, formato=True)}")
    print('_'*30) 