nm = int(input('Escreva um número inteiro: '))
print('Escolha uma das bases para ser convertida')
print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(bin(nm)[2:])
elif opcao == 2:
    print(oct(nm)[2:])
elif opcao == 3:
    print(hex(nm)[2:]) 
else:
   print('Opção inválida!')