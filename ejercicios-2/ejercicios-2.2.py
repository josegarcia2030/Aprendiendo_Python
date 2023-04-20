#creando una funcion que nos devuelve los numeros primos
#entre 0 y el argumento que le pasamos

#crear una funcion que verifique si un numero es primo
def es_primo(num):
    #verificamos que el numero pasado es primo
    for i in range(2,num-1):
        if num % i == 0:
            return False
    #si termina el bucle, significa que no fue divisible entoces no es primo
    return True

#creando funcion que retorne una lista con todos los primos
def primo_hasta(num):
    #creamos la lista
    primos = []
    for i in range(3,num + 1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de que sea lo agregamos a la lista
        if resultado == True:
            primos.append(i)
    #devolvemos la lista        
    return primos

#creamos el resultado llamando a la funcion y lo mostramos
resultado = primo_hasta(98)
print(resultado)
