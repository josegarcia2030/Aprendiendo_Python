#Datos compuestos

#1.- Listas == es una matriz
lista = ["Lucas Dalto", "Soy Dalto", True, 1.70]
print(lista)

for listas in lista:
    print(listas)
    

#2.- Tuplas == No se puede modificar
tupla = ("enrique","rasek2030", False, 26)
print(tupla)

for tuplas in tupla:
    print(tuplas)
    

#3.- Set (conjunto) == No se puede cambiar los elementos del conjunto
#No se puede acceder por indice [i], no almacena datos duplicados
conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.69}
print(conjunto)


#4.- DICCIONARIO
#key : value
#clave: valor

diccionario = {
    'nombre' : "lucas dalto",
    'canal' : 'soy dalto',
    'trabaja' : False,
    'altura': 1.59,
}

print(diccionario['nombre'])
print(diccionario['altura'])


