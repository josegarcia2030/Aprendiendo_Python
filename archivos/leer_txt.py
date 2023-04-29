#leer archivos .txt
archivo_sin_leer = open("archivos\\tipoDatos.txt", encoding="UTF-8")
#archivo = archivo_sin_leer.read()

#leer en especifico una linea del archivo
#linea_1 = archivo_sin_leer.readlines()


#leer una sola linea
linea = archivo_sin_leer.readline()
print(linea)


#cerrar el archivo
archivo_sin_leer.close()