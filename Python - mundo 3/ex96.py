def title():
    print(' Controle de Terrenos')
    print('----------------------')

def area():
    largura = float(input('LARGURA(m): '))
    comprimento = float(input('COMPRIMENTO(m): '))
    print(f'A area de um terreno de {largura}x{comprimento} e de {largura*comprimento:.2f}m2')

title()
area()

