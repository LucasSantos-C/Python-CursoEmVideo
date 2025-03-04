nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()

print(f"seu primeiro nome é: {n[0]}")
print(f"Seu último nome é: {n[-1]}")