expr = str(input('Digite a expressao: '))
pilha = list()

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressao foi valida')
else:
    print('Nao e valida')