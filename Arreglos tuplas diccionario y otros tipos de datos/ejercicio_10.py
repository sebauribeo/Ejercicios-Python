print('========================================')
dicc = {'gato':'cat', 'ave':'bird', 'dog':'perro'};
def verDicc():
    key = str(input('escribe la palabra en español: '))
    print('========================================')
    print(key, 'en español es ', dicc.get(key), 'en ingles' )
verDicc()    
print('========================================')
