print('========================================')
print('Ingresa 10 números para completar la tupla')
print('========================================')
tupla = ()
for i in range(10):
    (numero)= int(input('Ingresa tus numeros '))
    tupla = tupla+(numero,)
print('========================================')
print('Tu Tupla es: ',tupla)
print('mayor ',max(tupla));
print('menor ',min(tupla));
print('suma total ',sum(tupla));
print('Tupla ordenada ',sorted(tupla));
print("Elemento repetido ", tupla.count(numero), " veces")
print('========================================')

