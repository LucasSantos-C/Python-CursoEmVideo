nome = input('Escreva seu nome completo: ')
dividido = nome.split()

print(f"Maiúsculo: {nome.upper()}")
print(f"Minúsculo: {nome.lower()}")
print(f"Letras sem espacos: {len(nome.replace(" ",""))}")
print(f"Letras o primeiro nome: {len(dividido[0])}")
