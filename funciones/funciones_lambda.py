#funciones lambda
multiplicar_por_dos = lambda x : x * 2
#print(multiplicar_por_dos(10))

suma_por_dos = lambda x : x + 2
#print(suma_por_dos(15))

#creando funcion simple si es par
def es_par(num):
    if(num % 2 == 1):
        return True

#usando filter con una funcion comun
numeros = [1,2,3,4,5,6,7,8,9]
numeros_pares = filter(es_par, numeros)
#print(list(numeros_pares))


#creando con lambda
numeros_pares_lambda = filter(lambda numero: numero % 2 == 1, numeros)
#print(list(numeros_pares_lambda))





def pedirCantidad():
    cantidad = int(input("Escribe la cantidad\n"))
    return cantidad

def llenarLista(cantidad):
    edades = []
    for c in range(cantidad):
        edad = int(input("Escribe la edad porfavor:\n"))
        lista_edades = (edad)
        edades.append(lista_edades)
    return edades






