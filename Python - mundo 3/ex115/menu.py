from time import sleep
from os import system

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor digite um número Inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print("\033[31mEntrada interrompida pelo usuário.\033[m")
            return 0
        else:
            return n

def linha(tam = 42):
    return "-" * tam

def titulo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def VerCadastro():
    system('cls')
    titulo("LISTA DE PESSOAS")
    sleep(2)
    system('cls')
    
def CadastrarPessoas():
    system('cls')
    titulo("CADASTRO")
    sleep(2)
    system('cls')

def menu(lista):
    titulo("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c+=1
    print(linha())
    opc = leiaInt("\033[32mSua opção: \033[m")
    return opc


