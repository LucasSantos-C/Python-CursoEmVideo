'''def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)

mensagem('     SISTEMA DE ALUNOS')
mensagem('     FODA-SE')'''
"""
def soma(a,b):
    print(f'A = {a} e B = {b}')
    print(a+b) 


soma(a=4,b=5)"""
'''
def contador(*num):
    for v in num:
        print(v)


contador(2, 1, 7)
contador(2, 1, )
contador(2, 1, 7, 8 ,7)'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7,2,5,0,4]
dobra(valores)
print(valores)