from menu import *

while True:
    resp = menu(["Ver pesssoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"])
    if resp == 1:
        VerCadastro()
    elif resp == 2:
        CadastrarPessoas()
    elif resp == 3:
        print("\033[31mEncerrando programa...\033[m")
        sleep(2)
        break
    else:
        print("\033[31mErro: Digite algo válido\033[m")