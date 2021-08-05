import math

#ejercicio 1
radio = float (input ('Ingrese el radio de la circunferencia'))
perimetro = 2*math.pi*radio
print ("El perimetro de la circunferencia es: ", perimetro)

#ejercicio 2
radio = float (input('Ingrese el radio de la circunferencia '))
diametro = 2*radio
print ('El Diametro de la circunferencia es: ', diametro)

#ejercicio 3
radio = float (input('Ingrese el area de un circulo '))
area = math.pi*radio**2
print ('El area del circulo es: ', area)

#ejercicio 4
radio = float(input('Ingresa el volumen a calcular de la esfera '))
volumen = 4/3*math.pi*radio**3
print ('El volumen de la esfera es: ', volumen)

#ejercicio 5
cuadrado = float (input('Ingresa el perimetro de un cuadrado '))
areaC = cuadrado**2
print ('El volumen del cuadrado es: ', areaC)

#ejercicio 6
cubo = float (input('Ingrese el radio del cubo a calcular '))
radioCubo = cubo**3
print ('El volumen del cubo es: ', radioCubo)

#ejercicio 7
base = float(input('Ingresa la base del triangulo '))
altura = float(input('Ingresa la altura del triangulo '))
triangulo = (base*altura)/2
print ('El area del triangulo es: ', triangulo)

#ejercicio 8
base1 = float(input('Ingrese el valor de la base superior '))
base2 = float(input('Ingrese el valor de la base inferior '))
altura1 = float(input('Ingresa la altura'))
trapezoide = 1/2*(base1+base2)*altura1
print ('El area del trapezoide es: ', trapezoide)

#ejercicio 9
baseParalelogramo = float(input('Ingrese el valor de la base del paralelogramo '))
alturaParalelogramo = float(input('Ingrese la altura del paralelogramo '))
paralelogramo = baseParalelogramo*alturaParalelogramo
print ('El area del paralelogramo es: ', paralelogramo)

#ejercicio 10
alturaCilindro = float(input('Ingrese el valor de la altura del cilindro '))
radioCilindro = float(input('Ingrese el valor del radio del cilindro '))
volumecilindro = math.pi*radioCilindro**2*alturaCilindro
areaCilindro = 2*math.pi*radioCilindro**2+2*math.pi*radioCilindro*alturaCilindro
print ('El volumen del cilindro es: ', volumecilindro, ' y el area es: ', areaCilindro)
