diccionario = {
    "nombre" : "lucas",
    "apellido" : "dalto",
    "subs": 100000
}

#obteniendo un elemento dict_item iterable
iterable = (diccionario.items())
for i in iterable:
    print(i)



#nos devuelve un objeto dict_item
claves = diccionario.keys()
print(claves)

#obteniendo un elemento con get() sino encuentra nada el programa continua
print(diccionario.get("hola"))


#elimina todo del diccionario
#diccionario.clear()
#print(diccionario)



#elemento un elemento del diccionario
diccionario.pop("nombre")
print(diccionario)


