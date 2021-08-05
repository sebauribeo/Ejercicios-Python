
rutPersona = {11234345:"Diego Eguiguren",
              9876567:"Rosa Eguiguren",
              20987654:"Marcela Díaz",
              21234987:"Cristóbal Pérez"}
rutPersonaLista = list(rutPersona.keys())

def getPersona(rut):
    if rut in list(rutPersona.keys()):
        print(rutPersona[rut])
    else:
        print("El rut no existe.")
        
getPersona(21234987)