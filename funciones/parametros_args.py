#forma no optima de sumar valores

def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados


mi_lista = [5,3,9,10,20,3]
resultado = suma(mi_lista)
print(f'El resultado de la suma de la lista es : {resultado}')