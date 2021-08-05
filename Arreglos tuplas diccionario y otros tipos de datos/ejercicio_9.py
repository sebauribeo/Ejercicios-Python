a = (1,3,5,6,8,34,45,0,54);
b = (5,3,21,45,0,4,7,2,1,8);
def tuplas (tupla1, tupla2):
    contador = 0;
    comun = ();
    for i in tupla1:
        for j in tupla2:
            if j == i not in comun:
                contador += 1
                comun = comun+(j,)
    print ('Cantidad de numeros repetidos en las tuplas es: ', contador)            
    print('Los numeros comunes entre las tuplas son: ',comun)  
tuplas(a, b)
