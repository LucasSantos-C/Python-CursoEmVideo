"""
#escopo de variáveis
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
"""

#Retorno de valores
"""
def somar(a=0,b=0,c=0):
    s = a+b+c
    return s

r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)

print(r1, r2, r3)
"""

def fatorial (num=1):
    f = 1
    for i in range (num, 0, -1):
        f *= i
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(1)
 
print(f'Fatoriais: {f1}, {f2}, {f3}')