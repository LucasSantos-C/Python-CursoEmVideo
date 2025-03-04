from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
pergunta = 0

while pergunta != 5:
    print('''     -=-=-=-=-=-=-=-=-=-
    [ 1 ] Somar valores
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa!
    -=-=-=-=-=-=-=-=-=-=-''')
    pergunta = int(input('Selecione sua opção: '))
    if pergunta == 1:
        print('Processando valores...')
        sleep(1)
        print(f'A soma de {n1} + {n2}: {n1 + n2}')
        sleep(1)
    if pergunta == 2:
        print('Processando valores...')
        sleep(1)
        print(f' multiplicação entre {n1} x {n2}: {n1 * n2}')
        sleep(1)
    if pergunta == 3:
        print('Processando valores...')
        sleep(1)
        if n1 > n2:
            print(f'Maior número: {n1}')
        else:
            print(f'Maior número: {n2}')
        sleep(1)
    if pergunta == 4:
        print('Processando valores...')
        sleep(1)
        print("=-=-=-=-=-=-=-=-=-=-=-=-=")
        print('Escreva os novos valores!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('Processando novos valores...')
        sleep(1)
    elif pergunta > 5:
        print('Digite algo valido!!')
        sleep(1)
print('Finalzando ...')
sleep(1)
print('Fim do programa!!')
