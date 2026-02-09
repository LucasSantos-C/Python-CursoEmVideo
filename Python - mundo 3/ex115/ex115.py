from menu import *
from arquivo import *

arq = 'coisas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(["Ver pesssoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        titulo("CADASTRAR PESSOA")
        nome = input("Nome: ")
        idade = leiaInt("Idade: ")
        cadastrarPessoa(arq, nome, idade)
    elif resp == 3:
        print("\033[31mEncerrando programa...\033[m")
        sleep(2)
        break
    else:
        print("\033[31mErro: Digite algo válido\033[m")
    sleep(2)
