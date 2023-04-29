#abriendo el archivo
with open("archivos\\tipoDatos.txt", encoding="UTF-8") as archivo:
    #leemos el archivo
    print(archivo.read())