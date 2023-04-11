cadena1 = "Hola soy Rasek"
cadena2 = "Bienvenido Enrique2030"

#utilizamos la funcion dir
resultado = dir(cadena1)

#convertimos a mayuscula con el metodo upper
mayuscula = cadena1.upper()

#convertimos a minuscula con el metodo lower
minuscula = mayuscula.lower()

#1er letra mayuscula con el metodo capitalize
capital = cadena1.capitalize()


#buscamos una cadena en otra cadena, sino hay coincidencia devuelve -1 con el metodo fin
busqeda_find = cadena1.find("r")

#buscamos una cadena en otra cadena, sino hay coincidencia lanza una execepcion con el metodo index
busqueda_index = cadena1.index("a")


#si es numerico es Treue sino es False
es_numerico = cadena1.isnumeric()

#si es alfa numerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena2.isalpha()

#print(resultado)
print(mayuscula)
print(minuscula)
print(capital)
print(busqeda_find)
print(busqueda_index)
print(es_numerico)
print(es_alfanumerico)