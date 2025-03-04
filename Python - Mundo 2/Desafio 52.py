n1 = int(input('Digite um número: '))
count = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end='')
        count += 1
    else:
        print('\033[31m', end='')
    print(c, end = ' ')
print(f'\n\033[mO número {n1} foi divisível {count} vezes ', end = '')

if count == 2:
    print('\033[32mÉ PRIMO')
else:
    print('\033[31mNão é PRIMO')