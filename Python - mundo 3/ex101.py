from datetime import datetime

def voto(nasc):
    idade = (datetime.now().year) - nasc
    if idade < 16:
        return (f"Com {idade} anos: VOTO NEGADO")
    elif idade < 18 or idade >= 65:
        return (f"Com {idade} anos: VOTO OPCIONAL")
    else:
        return (f"Com {idade} anos: VOTO OBRIGATÓRIO")

ano = int(input("Em que ano você nasceu? "))
print(voto(ano))