vogais = ('a','e','i','o','u')
palavra = ('APRENDER','PROGRAMAR','LINGUAGEM',
           'PYTHON','CURSO','GRATIS','ESTUDAR',
           'PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')

for i in palavra:
    print(f'\nNa palavra: {i} temos as vogais:',end=' ')
    for letra in i:
        if letra.lower() in vogais:
            print(letra,end='')
