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
    


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor digite um número Real!\033[m')
        except KeyboardInterrupt:
            print("\033[31mEntrada interrompida pelo usuário.\033[m")
            return 0
            break
        else:
            return n
    
def main():
    i = leiaInt("Digite um número Inteiro: ")
    f = leiaFloat("Digite um número Real: ")
    print(f"O usuário digitou os números {i} e {f:.2f}")

main()
