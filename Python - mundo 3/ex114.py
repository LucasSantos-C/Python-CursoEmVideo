import requests

def EstaNoAr(url, timeout=5):
    try:
        resposta = requests.get(url, timeout=timeout)
        print("Está no ar.")
    except requests.RequestException:
        print("\033[0;31mERRO: site fora do ar.\033[m")

conect = EstaNoAr("https://pudim.com.br/")