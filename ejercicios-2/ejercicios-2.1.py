#falto el profe y los pibes van a armar la clase

#pedir el nombre y la edad de los compañeros que vinieron
#hoy a clases


def obtener_compañeros(cantidad):

    compañeros = []
    #ejecutandoun for para pedir informacion de cada compañero
    for i in range(cantidad):
        nombre = input("ingrese el nombre del compañero:\n")
        edad = int(input("ingrese la edad del compañero:\n"))
        compañero = (nombre, edad)
        #agregando la informacion a la lista
        compañeros.append(compañero)
    
    #ordenando de menor a mayor segun su edad
    compañeros.sort(key=lambda x:x[1])

    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]


    #retornamos una tupla
    return asistente,profesor

#asistente, profesor = obtener_compañeros(5)
#print(f'El profesor es : {profesor} y el asistente es : {asistente}')




#Crear una lista de contactos
def lista_contactos(cantidad_contactos):
    lista = []
    for i in range(cantidad_contactos):
        nombre = input("Ingresa el nombre de tu contacto\n")
        celular = input("Ingresa su numero de celular\n")
        direccion = input("Ingresa la direccion del contacto\n")
        edad = int(input("Ingresa la edad de tu contacto\n"))

        contactos = (nombre, celular, direccion, edad)
        lista.append(contactos)

    print(lista)


cantidad_agregar = int(input("Que cantidad de contactos vas a agregar\n"))
lista_contactos(cantidad_agregar)






