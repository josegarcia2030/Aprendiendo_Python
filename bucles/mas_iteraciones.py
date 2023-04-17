#
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
for fruta in frutas:
    print(fruta)

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'Me voy a comer : {fruta}' )


#evitar que el bucle siga ejecutandose, el else tampoco se ejecuta
for fruta in frutas:
    if fruta == 'pera':
        break
else:
    print("terminado")




#iterar una cadena de texto (recorrer)
cadena = "Hola dalto"
for letra in cadena:
    print(f'{letra}')


#
numeros =[2,5,8,10]
numeros_duplicados = list()

for numero in numeros:
    numeros_duplicados.append(numero * 2)
print(numeros_duplicados)

#for en una sola linea de codigo(duplicamos los numeros)
numeros_duplicados_dos = [ n*2 for n in numeros]
print(numeros_duplicados_dos)









