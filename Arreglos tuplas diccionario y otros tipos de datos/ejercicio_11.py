print('========================================')
print('Ingresa el RUT para saber el nombre de la persona')
print('========================================')
print('OPCIONES')
print('========================================')
print('123456789 \n987654321 \n432145678 \n321453456')
print('========================================')
dicc = {123456789:'Seba', 987654321:'Evelyn', 432145678:'Naty', 321453456:'Dexter'};
key = int(input('Introduce el rut '))
print('========================================')
if key == key:
    print('Haz ingresado el rut correspondiente a:', dicc.get(key))
else:
    print('Rut invalido')
print('========================================')
