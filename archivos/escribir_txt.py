with open("archivos\\tiposDatos.txt", "w", encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("Se cambiaron los valores")
    archivo.writelines(["Hola","Bienvenido"])