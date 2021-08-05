#EJERCICIO 1
print('========================================')
cont=10
while cont<110:
  print (cont)
  cont=cont+10
print('========================================')

#EJERCICIO 2
print('========================================')
val1= int(input('Ingresa tu primer valor '))
val2= int(input('Ingresa tu segundo valor '))
print('========================================')
print ('Los número pares entre ', val1, ' y ', val2, ' es:')
while val1<=val2:
    print(val1)
    val1=val1+2
print('========================================')


#EJERCICIO 3
print('========================================')
impar=1
while impar<=50:
  print (impar)
  impar=impar+2
print('========================================')

#EJERCICIO 4
print('========================================')
base= int(input('Ingresa el valor de base '))
exponente= int(input('Ingresa el valor de exponente '))
resultado = 1
for i in range(exponente):
  resultado *= base
print('========================================')
print ('El resultado de la potencia de ', base, ' elevado a ', exponente, ' es: ',resultado)
print('========================================')

#EJERCICIO 5
print('========================================')
n=int(input("Ingrese un número "))
contar=0
factorial=1
while contar<n:
    contar=contar+1
    factorial=factorial*contar
print("El factorial de ",n," es ",factorial)
print('========================================')
