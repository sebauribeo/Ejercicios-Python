import math

x = int(input('ingresa un número'))
y = int(input('ingresa otro número, distinto al anterior'))
if x < y:
    print(x, 'es menor que '. y)
else:
    print(x, 'es mayor que', y)    
print('========================================')


x1 = int(input("Ingresa un número entero"))
if x1 < 0:
 print("El número es negativo")
elif x > 0:
 print('El número es positivo')
else:
 print('El número es cero')
print('========================================')


#ejercicio 1
compra = float(input('Ingresa el valor de tu compra '))
if compra >= 100000:
    print ('Tu compra tiene un 10 porciento de descuento')
else:
    print ('Tu compra tienen un 5 porciento de descuento')
print('========================================')


#ejercicio 2
notas = float(input('Ingresa tu promedio de notas '))
asistencia = float(input('Ingresa tu porcentaje de asistencia '))
if notas >= 4.0:
    print('Haz aprobado, tu promedio de notas es mayor o igual a 4.0')
else:
    print('Haz reprovado, tu promedio de notas es menor a 4.0')

if asistencia >= 60:
    print ('Alumno aprobado, tu porcentaje es mayor a 60%')    
else:
    print ('Alumno reprovado, tu porcentaje de asistencia es menor a 60%') 
print('========================================')


#ejercicio 3
celcius = float(input('Ingresa la cantidad de grados celcius a calcular '))    
farenheit = float(input('Ingresa la cantidad de grados farenheit a calcular '))
calculoFarenheit = (farenheit - 0)*5/9
calculoCelcius = (celcius * 9/5) + 32
print ('Los °C ingresados son ', calculoCelcius,'° convertidos a Farenheit')
print ('Los °F ingresados son ', calculoFarenheit,'° convertidos a Celcius')
print('========================================')


#ejercicio 4 
pesos = float(input('Ingresa la cantidad de pesos chilenos a calcular '))    
dolares = float(input('Ingresa la cantidad de dolares a calcular '))
calculoPesos = pesos/720
calculoDolar = 720*dolares
print ('Los pesos chilenos ingresados son ', calculoPesos,' dolares')
print ('Los dolares ingresados son ', calculoDolar,' pesos chilenos')
print('========================================')


# #ejercicio 5
pesos1 = float(input('Ingresa la cantidad de pesos chilenos a calcular '))    
euros = float(input('Ingresa la cantidad de euros a calcular '))
print ('Opciones')
print ('1.- Pesos a Euro')
print('2.- Euro a pesos')
calculo = float(input('Ingresa tu opcion'))
if calculo == 1:
    calculoPesos = pesos1/850
    print ('Los pesos chilenos ingresados son ', calculoPesos,' euros')
elif calculo == 2:
    calculoEuros = 850*euros
    print ('Los euros ingresados son ', calculoEuros,' pesos chilenos')
print('========================================')


#ejercicio 6
grados = float(input('Ingresa la cantidad de grados para calcular a radianes '))    
radianes = float(input('Ingresa la cantidad de radianes para calcular a grados '))
print('Opciones')
print('1- Grados a Radienes')
print('2.-Radienes a Grados')
calculo2 = float(input('Ingresa tu opcion'))
if calculo2 == 1:
    calculoGrados = grados*math.pi/180
    print ('Los grados ingresados son ', calculoGrados,'° convertidos a Radienes')
elif calculo2 == 2:  
    calculoRadianes = radianes*180/math.pi 
    print ('Los Radienes ingresados son ', calculoRadianes,'° convertidos a Grados')
print('========================================')


#ejercicio 7
print('Calcula tu edad de tu perrro en años humanos')
edad_p = int(input('Ingresa la edad de tu perro '))
if edad_p == 1:
    print('Tu edad de tu perro en años humanos es: ', edad_p + 10.5)
elif edad_p == 2:
    print('Tu edad de tu perro en años humanos es: ', edad_p + 21)
elif edad_p > 2:
    print('Tu edad de tu perro en años humanos es: ', edad_p * 4 + 21)
elif edad_p < 1:
    print('Ingresa un número positivo o mayor a cero')  
print('========================================')


#ejercicio 8
print ('¿Deseas saber tu masa corporal?')
print ('Opciones')
print ('1.- si')
print ('2.- no')
dec =float(input('Ingresa tu opcion'))
if dec == 1:
    peso = float(input('Ingresa tu peso en kg'))
    altura = float(input('Ingresa tu altura en mt'))
    masa = peso/(altura**2)
    print ('Tu mas corporal es: ', masa)
else:
    print ('Que tengas buen dia!')
print('========================================')


# ejercicio 9
print ('Elije tu sexo')
print ('Opciones')
print ('1.- Hombre')
print ('2.- Mujer')
sexo = float(input('Ingresa tu opción '))
if sexo == 1:
    pesoHombre = float(input('Ingresa tu peso '))
    alturaHombre = float(input('Ingresa tu altura '))
    años = float(input('Ingresa tu edad '))
    TMB = 66.5+(13.8*pesoHombre)+(5*alturaHombre)-(6.8*años)
    print ('Tu tasa metabolica basal es: ', TMB)
    print('========================================')
elif sexo == 2:    
    pesoMujer = float(input('Ingresa tu peso'))
    alturaMujer = float(input('Ingresa tu altura'))
    añosM = float(input('Ingresa tu edad'))
    TMB_M = 655+(9.6*pesoMujer)+(1.85*alturaMujer)-(4.7*añosM)
    print ('Tu tasa metabolica es: ', TMB_M)
    print('========================================')
else:
    print ('Opcion invalida')
print('========================================')   


# ejercicio 10
monto = 500000
print('Tu monto es de $',monto)
print('Opciones:')
print('-1. Deposito')
print('-2. giro')
proceso = int(input('Ingresa la opcion que deceas realizar '))
if proceso == 1:
    deposito = int(input('Cual es el monto de tu deposito '))
    print('El monto total de tu saldo es: ', monto+deposito)
elif proceso == 2:
    giro = int(input('Ingresa el monto que deceas retirar '))
    print('Haz retirado $',giro, 'de tu cuenta, tu moto actual es de $',monto-giro )
    if giro > monto:
        print('No puedes retirar mas que tu saldo total')
elif proceso > 2:
    print('La opcion que elegiste no es valida')
else:
    proceso < 1
    print('La opcion que ingresaste es invalida') 
print('========================================')
   