dicc_1 = {} 
print("""
Selecciones una de las siguientes opciones
------------------------------------------
1.- Agregar poroductos
2.- Ver productos
3.- Salir
------------------------------------------
""")
repeticion = int(input('Ingresa tu opcion '))   
while repeticion == 1:
    print('------------------------------------------')
    key = int(input('Ingresa tu codigo '))
    print('------------------------------------------')
    prod = str(input('Ingresa el nombre de tu producto '))
    print('------------------------------------------')
    precio = int(input('Ingresa el precio de tu producto '))
    dicc_1[key] = [prod, precio]
    print('------------------------------------------')
    print("""
Como deceas continuar?
------------------------------------------
1.- Agregar poroductos
2.- Ver productos
3.- Salir
------------------------------------------
""")
    repeticion = int(input('Ingresa tu opcion '))
    print('------------------------------------------')
if repeticion == 2:
    print("""
DETALLE PRODUCTOS: 
------------------------------------------
Codigo\tProducto\tPrecio
------------------------------------------""")
    for i in dicc_1:
        print(i,'\t',dicc_1[i][0],'\t\t',dicc_1[i][1]) 
if repeticion == 3:        
    print('------------------------------------------')
    print('Hasta la proxima')
    print('------------------------------------------')

    
