#variables

cadena1 = "Hola,soy,Dalto"
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


#Nos devuelve true si es numerico
is_numerico = cadena1.isnumeric()
print(is_numerico)

#Si es alfanumercio devuelve True
is_alfa_numerico = cadena1.isalpha()
print(is_alfa_numerico)

#buscamos una cadena en otra cadena, devuelve la cantidad de veces la coincidencia
contar_coincidencia = cadena1.count("a")
print(contar_coincidencia)


#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)
print(contar_caracteres)



#verificamos si una cadena empieza con otra cadena dada
empieza_con = cadena1.startswith("H")
print(empieza_con)


#verificams si termina con una cadena dada
termina_con = cadena1.endswith("o")
print(termina_con)


#reemplza una parte de la cadena, por otra
print(cadena1)
cadena_nueva = cadena1.replace(",", " ")
print(cadena_nueva)


#separa cadena con la cadena que le pasemos
cadena_separada = cadena1.split(",")
print(cadena_separada)
print(type(cadena_separada))
for cadena in cadena_separada:
    print(cadena)