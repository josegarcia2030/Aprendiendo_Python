
diccionario = {
    "nombres": "jose",
    "apellido": "garcia",
    "apodo":"rasek2030"
}


for key in diccionario.items():
    #print(key)
    pass

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La claves : {key} y el valor es : {value}')