dicc_1 = {} 
print('------------------------------------------')
print("""
    Selecciones una de las siguientes opciones
    ------------------------------------------
    1.- Agregar usuario y contraseña
    2.- Ver usuarios
    3.- Editar usuario y contraseña
    4.- Borrar usuario
    5.- Salir
    ------------------------------------------
    """)
repeticion = int(input('Ingresa tu opcion ')) 
while repeticion == 1:
    print('------------------------------------------')
    rut = int(input('Ingresa el rut de tu usuario sin guion '))
    print('------------------------------------------')
    usuario = str(input('Ingresa el nombre de usuario '))
    if usuario.lower() == False:
        print('Tu usuario debe ser solo con minusculas')
        print('------------------------------------------')
        if  len(usuario) == 0:
            print('Este campo no debe estar vacio')
            print('------------------------------------------')
    print('------------------------------------------')
    contrasena = input('Ingresa tu contraseña ')
    print('------------------------------------------')
    if len(contrasena)<8:
        print("Tu contraseña debe tener un minimo de 8 caracteres")
        print('------------------------------------------')
        if  len(contrasena) == 0:
            print('Este campo no debe estar vacio')
            print('------------------------------------------')
    dicc_1[rut] = [usuario, contrasena]
    print('------------------------------------------')
    print("""
    Como deceas continuar?
    ------------------------------------------
    1.- Agregar otro usuario y contraseña
    2.- Ver usuarios
    3.- Editar usuario y contraseña
    4.- Borrar usuario
    5.- Salir
    ------------------------------------------
    """)
    repeticion = int(input('Ingresa tu opcion '))
    if repeticion == 2:
        print("""
DETALLE USUARIOS: 
------------------------------------------
RUT\t NOMBRE\t\t CONTRASEÑA
------------------------------------------""")
        for i in dicc_1:
            print(i,'\t',dicc_1[i][0],'\t\t',dicc_1[i][1])
        print('------------------------------------------')
        print("""
    Selecciones una de las siguientes opciones
    ------------------------------------------
    1.- Agregar usuario y contraseña
    2.- Ver detalle  usuarios
    3.- Editar usuario y contraseña
    4.- Borrar usuario
    5.- Salir
    ------------------------------------------
    """)
        repeticion = int(input('Ingresa tu opcion '))     
    if repeticion == 3:
        print('------------------------------------------')
        rut = int(input('Ingresa el rut a editar de tu usuario sin guion '))
        print('------------------------------------------')
        usuario = str(input('Ingresa el nombre de usuario a editar '))
        if usuario.lower() == False:
            print('Tu usuario debe ser solo con minusculas')
            print('------------------------------------------')
            if  len(usuario) == 0:
                print('Este campo no debe estar vacio')
                print('------------------------------------------')
        print('------------------------------------------')
        contrasena = input('Ingresa tu nueva contraseña ')
        print('------------------------------------------')
        if len(contrasena)<8:
            print("Tu contraseña debe tener un minimo de 8 caracteres")
            print('------------------------------------------')
            if  len(contrasena) == 0:
                print('Este campo no debe estar vacio')
                print('------------------------------------------')
        dicc_1.update({rut : [usuario,contrasena]})
        print('Diccionario actual ',dicc_1)
        print('------------------------------------------')
        print("""
    Como deceas continuar?
    ------------------------------------------
    1.- Agregar otro usuario y contraseña
    2.- Ver usuarios
    3.- Editar usuario y contraseña
    4.- Borrar usuario
    5.- Salir
    ------------------------------------------
    """)
        repeticion = int(input('Ingresa tu opcion '))
        print('------------------------------------------')
    if repeticion == 4:
        usuario = str(input('Ingresa el RUT de usuario a eliminar '))
        print('------------------------------------------')
        dicc_1.pop(rut)
        print('Diccionario actual ',dicc_1)
        print('------------------------------------------')
        print("""
    Como deceas continuar?
    ------------------------------------------
    1.- Agregar otro usuario y contraseña
    2.- Ver usuarios
    3.- Editar usuario y contraseña
    4.- Borrar usuario
    5.- Salir
    ------------------------------------------
    """)
        repeticion = int(input('Ingresa tu opcion '))
        print('------------------------------------------')
    if repeticion == 5:        
        print('------------------------------------------')
        print('Hasta la proxima')
        print('------------------------------------------')