n=int(input("Ingrese un número "))
suma=0
for i in range (1,n):
    if n%i==0:
        suma=suma+i
if suma==n:
    print("El número es perfecto")
elif suma>n:
    print("El número es abundante")
else:
    print("El número es defectivo")
