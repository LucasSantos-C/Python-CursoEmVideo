import menu
from time import sleep
from os import system

def main():
    menu.MenuPrincipal()
    while True:
        try:
            option = int(input("Sua Opção: "))
            if option == 1:
                menu.VerCadastro()
                system('cls')
                menu.MenuPrincipal()
            elif option == 2:
                menu.CadastrarPessoas()
                system('cls')
                menu.MenuPrincipal()
            elif option == 3:
                print("Encerrando o Programa...")
                sleep(1)
                break
            else:
                    print("Erro: Digite uma opção válida")
        except (ValueError, TypeError):
                print("Erro: você digitou algo errado")

main()