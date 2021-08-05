import math
print('========================================')
a = float(input('Ingresa el valor de A: '));
while a < 1:
    print('Tu número debe ser mayor a cero')
    a = float(input('Ingresa el valor de A: '));

print('========================================')
b = float(input('Ingresa el valor de B: '));
while b < 1:        
    print('Tu número debe ser mayor a cero')
    b = float(input('Ingresa el valor de B: '));

print('========================================')
c = float(input('Ingresa el valor de C: '));
while c < 1:        
    c = float(input('Ingresa el valor de C: '));
    print('Tu número debe ser mayor a cero')

print('========================================')
print('Tus números elegidos son: ', int(a),' - ', int(b),' - ', int(c))

print('========================================')

x = math.pow(-b, b**2)-4*a*c/2*a
print('El valor de X es: ', int(x))

print('========================================')
positivo = b**2-4*a*c
if positivo < 0:
    print('Tu resultado salio negativo')
    print('========================================')
    x=-b/2*a
    y = (b**2-4*a*c)-(1/2)
    i = -1**(1/2)
    z=x+y*i
    print('Tu número complejo es: ', int(z))
print('========================================')


