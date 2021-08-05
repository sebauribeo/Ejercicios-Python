
#EJERCICIO1
def nombre():
  print('Nombre: Sebastian Uribe')
  print('Centro de estudios: Inacap')
  print('Año: 2021')
nombre()   

#EJERCICIO2 FACTORIAL
def factorial(numero):
    if numero>=1:
        f=numero
        while numero>=2:
            numero=numero-1
            f=f*(numero)
        print("el factorial es: ",f)
    if numero==0:
        print("el factorial es 1")
factorial(int(input("ingrese el numero para calcular su factorial: ")))
#EJERCICIO2 POTENCIA
def potencia(base, altura):
    return base ** altura
print ('El resultado es: ', potencia)
base = (int(input("ingrese el numero para calcular su factorial: ")))
altura = (int(input("ingrese el numero para calcular su factorial: ")))