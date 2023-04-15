#variables

cadena1 = "Hola soy Dalto"
cadena2 = "Bienvenido maquinola"

resultado = dir(cadena1)

#Nos imprime los metodos que podemos utilizar con las cadenas de textos
#print(resultado)

#Convertimos el texto a mayuscula
mayuscula = cadena1.upper()
print(mayuscula)

#Convertimos el texto a minuscula
minuscula = mayuscula.lower()
print(minuscula)

#Conevrtimos la primera letra a mayuscula
capital = minuscula.capitalize()
print(capital)


#buscar un valor que le pidamos
busqueda_find = cadena1.find("soy")
print(busqueda_find)

#buscar una cadena en otra cadena lanza una excepcion
busqueda_index = cadena2.index("m")
print(busqueda_index)