#Creando una lista con otra list()
lista = list(["hola", "soy", "dalto", 34, 2500, 69246604])

for listas in lista:
    print(listas)


#Nos devuelve la cantidad de elementos que tiene la lista 
cantidad_elementos = len(lista)
print(f'La cantidad de elementos son {cantidad_elementos}')



#agregando un elemento a la lista
print(lista)
lista.append(1.69)
for listas in lista:
    print(listas)


#agregar elemento a la lista con indice especifico
lista.insert(0,"inicio")
print(lista)


#agregamos varios elementos a la lista, con otra lista
lista.extend([False, 2030])
print(lista)


#eliminar un elemento de la lista por su indice

#Eliminamos el 1er elemento
lista.pop(0)
#eliminamos el ultimo elemento
lista.pop(-1)
print(lista)



#removiendo un elemento por su valor
lista.remove("soy")
print(lista)



#ordenando la lista
edades = [17,25,63,54,25,84,16,32]
edades.sort()
print(edades)



#invirtiendo la lista
edades.sort(reverse=True)
print(edades)



#otra forma de invertir
edades.reverse()
print(edades)




#eliminando todos los elementos de la lista
#lista.clear()
#print(lista)
#print(dir(lista))



#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(2500)
print(elemento_encontrado)
