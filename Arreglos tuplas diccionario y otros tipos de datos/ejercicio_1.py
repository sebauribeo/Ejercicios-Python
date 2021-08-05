 
while True:
    error=0
    usuario=input("Nombre de usuario: ")
    pass1=input("Contraseña: ")
    print('========================================')
    if usuario.islower() == False:
        print('Tu usuario debe ser solo con minusculas')
        error=1
        print('========================================')
    if len(pass1)<8:
        print("Tu contraseña debe tener un minimo de 8 caracteres")
        error=1
        print('========================================')
    if len(usuario) == 0:
        print('Tu usuario esta vacio')
        error=1
        print('========================================')
    if len(pass1) == 0:
        print('Tu contraseña esta vacia')
        print('========================================')
        error=1
    if error==0:
        print("Usuario registrado")
        break
print('========================================')




