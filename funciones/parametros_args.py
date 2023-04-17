#forma no optima de sumar valores
def sumar(a ,b):
    resultado = a + b
    print(f'El resultado de la suma es: {resultado}')

#sumar(10,30)

def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados


mi_lista = [5,3,9,10,20,3]
resultado = suma(mi_lista)
#print(f'El resultado de la suma de la lista es : {resultado}')



#utilizando el operador *(args) como argumento
def sumando(nombre, *numeros):
    resultado_suma = sum(numeros)
    return f'{nombre}, la suma de tu numeros es : {resultado_suma}'

print(sumando('enrique',5,3,9,10,20,3))













