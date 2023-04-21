


#variables
nombres = []
edades = []




def practicar():
    numero = int(input("Ingresa el numero con la cantidad de usuarios que ingresaras\n"))
    cont = 0
    while cont < numero:
        nombre = input("Ingresa el nombre de la persona\n")
        edad = int(input("Ingresa la edad de la persona\n"))
        nombres.append(nombre)
        edades.append(edad)
        cont += 1



def preguntar_cantidad():
    cantidad = int(input("Escribe la cantidad\n"))
    return cantidad


def preguntarNombre():
    nombre = input("Escribe el nombre de la persona\n")
    return nombre


def preguntarEdad():
    edad = int(input("Escribe la edad de la persona\n"))
    return edad


def agregarLista(cantidad):
    cont = 0
    while cont < cantidad:
        nombres.append(preguntarNombre())
        edades.append(preguntarEdad())
        cont += 1



'''agregarLista(3)
print(nombres)
print(edades)'''



def saber_mayor_menor():
    edad1 = int(input("Escribe la edad de Enrique\n"))
    edad2 = int(input("Escribe la edad de Frank\n"))

    if edad1 > edad2:
        print("La edad de Enqiue es mayor..")
    elif edad2 > edad1:
        print("La edad de Frank es mayor..")
    else:
        print("Los dos son de la misma edad")




def login():

    usuario = "Enrique"
    contraseña = "Rasek2030"

    user = input("Escribe el Usuario\n")
    password = input("Escribe la Contraseña\n")

    if user == usuario:
        if password == contraseña:
            print(f"Bienvenido {usuario}")
        else:
            print("Tu contraseña esta mal..")
    else:
        print("Tu usuario no es el correcto")

#login()


'''cont = 1

while cont <= 6:
    print(f'El numero es : {cont}')
    cont += 1 '''





#sueldo = float(input("Escribe tu sueldo\n"))



def saberSueldo():
    sueldo = float(input("Escribe el sueldo\n"))
    return sueldo

def descuentoSueldo(sueldo):
    descuento = (sueldo * 12.71) / 100
    return descuento

def sueldoNeto(sueldo, descuento):
    return sueldo - descuento

def mostrarSueldo(sueldo):
    print(f'El sueldo es Bs. {sueldo}')

def mostrarDescuento(descuento):
    print(f'Tu descuento de aportes es de Bs. {descuento}')

def mostrarSueldoNeto(neto):
    print(f'Tu sueldo neto sera de Bs. {neto}')



sueldo = saberSueldo()
descuento = descuentoSueldo(sueldo)
neto = sueldoNeto(sueldo, descuento)
mostrarSueldo(sueldo)
mostrarDescuento(descuento)
mostrarSueldoNeto(neto)































































