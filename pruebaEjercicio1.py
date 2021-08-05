print('========================================')
print('OPERACION MATEMATICA')
print('========================================')
num = int(input("Ingrese su primer número "))
numFactorial = int(input("Ingrese su segundo número "))
print('========================================')
contador = 0
factorial = 1
while contador < numFactorial:
    contador = contador + 1
    factorial=factorial*contador
print('el resultado de la operacion es ', num ** numFactorial / factorial)
print('========================================')
