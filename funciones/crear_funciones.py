#creando una funcion simple

def saludar():
    print("Hola, como estas?")

contador = 0
while contador < 2:
    contador += 1
    saludar()



#agregar una funcion que tenga un parametros
def saludamos(nombre):
    print(f'Hola {nombre} como estas?')

saludamos("enrique")



def pedirDatos():

    def pedirNombre():
        nombre = input('Bienvenido\nNos podrias decir tu Nombre :\n')
        return nombre.lower()

    def pedirGenero():
        dato = int(input("Por favor indica tu genero:\n" +
        "1.- Masculino\n" + 
        "2.- Femenino\n" + 
        "3.- otros\n"))
        if dato == 1:
            genero = "masculino"
        elif dato == 2:
            genero = "femenino"
        elif dato == 3:
            genero = "LGTB"
        else:
            genero = "No indicaste tu genero"
        return genero.lower()

    nombre = pedirNombre()
    genero = pedirGenero()


    def mostrarDatos(nombre, genero):
        print(f'Hola {nombre} te damos la bienvenida, tu genero es : {genero}')
    
    mostrarDatos(nombre, genero)



#pedirDatos()


#crear una funcion que nos retorne valores
def crear_password_random(num):
    caracter = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])

    c1 = num - 2
    c2 = num
    c3 = num - 5

    password = f"{caracter[c1]}{caracter[c2]}{caracter[3]}{num * 2}"
    return password


password = crear_password_random(1)
frase = f"Tu contraseña nueva es : {password}"
#print(frase)


#crear funcion que nos retorne multiples valores
def crear_password(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])

    c1 = num - 2
    c2 = num
    c3 = num - 5

    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return password, num


#desempaquetando la funcion 
password, numero = crear_password(981)

#mostrando los resultados obtenidos y los datos uitlizados para obtenerlos
print(f"Tu contraseña nueva es : {password}")
print(f'El numero utilizado para crearla fue {numero}')





