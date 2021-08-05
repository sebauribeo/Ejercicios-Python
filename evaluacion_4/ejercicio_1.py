print('------------------------------------------')
lista = []
print('Lista actual', lista[:])
print('------------------------------------------')
print("""
OPCIONES
------------------------------------------
1.- Agregar Nombre.
2.- Salir.
3.- Borrar.
------------------------------------------
""")
agregar = int(input('Ingresa tu opcion: '));
if agregar > 3 or agregar < 1:
    print('Haz ingresado la opcion incorrecta')
while agregar == 1:    
    nombre=str(input("Ingresa el nombre de mascota: "));
    print('------------------------------------------')
    lista.append(nombre)
    print('Lista actual', lista[:])
    print('------------------------------------------')
    print("""
OPCIONES
------------------------------------------
1.- Agregar nombre
2.- Salir
3.- Borrar ultimo nombre ingresado
------------------------------------------
""")
    agregar = int(input('Ingresa tu opcion: '))
while agregar == 3:
    lista.pop()    
    print('Nombre borrado')
    print('Lista actual', lista[:])
    print('------------------------------------------')
    print('Deceas seguir?')
    print('------------------------------------------')
    print("""
OPCIONES
------------------------------------------
1.- Agregar nombre
2.- Salir
3.- Borrar ultimo nombre ingresado
------------------------------------------
""")
    agregar = int(input('Ingresa tu opcion: '))
if agregar == 2:
    print('------------------------------------------')
    print ('Que tengas buen día!!!')  
    print('------------------------------------------')