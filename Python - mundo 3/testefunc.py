
def contador (i,f,p):
    #doctype
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da conagem
    :return: sem retorno
    """
    c=i
    while c <= f:
        print(f"{c}",end="..",flush=True)
        c += p
    print('FIM!')

help(contador)

#parâmetros opcionais
def somar(a=0,b=0,c=0):
    s = a+b+c
    print(f"A soma vale {s}")

somar(3,2,5)
somar(8,4)
somar()

