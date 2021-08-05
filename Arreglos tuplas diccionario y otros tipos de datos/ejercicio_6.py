acumulado = []
valor = int(input("¿Cuantos valores deseas ingresar?: "))
for i in range(1, valor + 1):
  insert = int(input("Ingrese el valor #{0}: ".format(i)))
  acumulado.append(insert)
def ordenar_max(acumulado):
  for i in range(len(acumulado)):
    for m in range(len(acumulado)):
      if acumulado[i] > acumulado[m]:
        tmp = acumulado[i]
        acumulado[i] = acumulado[m]
        acumulado[m] = tmp
  
  print("Lista ordenada", end=": ")
  for lt in range(len(acumulado)):
    print(acumulado[lt], end=":")
  print("Fin!!")
        
def ordenar_min(acumulado):
  for i in range(len(acumulado)):
    for m in range(len(acumulado)):
      if acumulado[i] < acumulado[m]:
        tmp = acumulado[m]
        acumulado[m] = acumulado[i]
        acumulado[i] = tmp
  
  print("Lista ordenada", end=": ")
  for lt in range(len(acumulado)):
    print(acumulado[lt], end=":")
  print("Fin!!")
print("""
\nSelecciones una de las siguientes opciones
------------------------------------------
1) Ordenar de mayor a menor
2) Ordenar de menor a mayor
------------------------------------------
""")
selec = int(input("Selecciones una opción: "))
if selec == 1:
  ordenar_max(acumulado)
elif selec == 2:
  ordenar_min(acumulado)