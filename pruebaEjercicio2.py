print('========================================')
print('CALCULAR NÚMEROS AMIGOS')
print('========================================')
def divisor (x):
    suma = int(0);
    for k in range(1, int(x / 2) + 1):
        if((x % k) == 0):
            suma = suma + k;
    return suma;
num1 = int(input("Ingresa tu primer número: "))   
num2 = int(input("Ingresa tu segundo Número: ")) 
print('========================================')
print (str(num1) + "\t" + str(num2) + '\tEstos son tus números escogidos',)
for i in range(num1, num2):
    resI = int(divisor(i)); 
    for j in range(i, num2):
        resJ = int(divisor(j));
        if((resI == j ) and (resJ == i)):
            print (str(i) + "\t" + str(j) + "\tSon número amigos");   
print('========================================')

