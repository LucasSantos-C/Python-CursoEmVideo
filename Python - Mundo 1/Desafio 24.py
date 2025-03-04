cd = str(input('Em que cidade voce nasceu? ').strip)
santo = cd.split(cd.upper())

if santo[0] == 'SANTO' or 'SÃO' or 'SAO':
    print(True)
else:
    print(False) 
