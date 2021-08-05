n=int(input("Ingrese un número "))
contar=0
for i in range(1,n):
    if n%i==0:
        print(i)
        contar=contar+1
if contar==1:
    print("El número es primo")
else:
    print("El número es compuesto")
