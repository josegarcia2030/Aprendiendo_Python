
#creando diccionarios en dict()
diccionario = dict(nombre="lucas", apellidos="dalto")
print(diccionario)


#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario1 = {("dalto", "lucas"): "jajaja"}
print(diccionario1)

diccionario2= {frozenset(["jose","garcia"]):"rasek2030"}
print(diccionario2)


#creando diccionario con fronkeys()
diccionario3 = dict.fromkeys(["nombre", "apellido","sucriptores"])
print(diccionario3) 

