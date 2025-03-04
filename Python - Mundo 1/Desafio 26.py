frase = str(input('Digite uma frase: ')).strip()

print(f'A letra A aparece {frase.upper().count("A")} vezes na frase')
print(f'A primeira letra A aparece na posicao: {frase.upper().find("A") + 1}')
print(f'A última letra A aparece na posicao: {frase.upper().rfind("A") + 1}')