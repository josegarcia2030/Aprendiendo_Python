
#Escriba un programa que pida al usuario que escriba su nombre, y lo salude llamandolo por su nombre

#pedir nombre al usuario
def pedirNombre():
    nombre = input("Escribe tu nombre:\n")
    return nombre

def saludar(nombre):
    print(f'Bienvenido {nombre}')



saludar(pedirNombre())