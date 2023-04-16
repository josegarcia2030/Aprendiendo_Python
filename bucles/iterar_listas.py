
animales_lista = ["pez","perro", "gato", "loro", "cocodrilo"]
for animal in animales_lista:
    print(animal)


# recorriendo la lista numeros y multiplicando x2
numeros = [52,10,62,12,72]
for num in numeros:
    print(num * 10)



#recorriendo 2 listas con 1 solo for
for numero,animal in zip(animales_lista, numeros):
    print(f"El animal es: {numero.capitalize()} y la cantidad que hay es: {animal}")



for num in range(10,100,10):
    print(num)


#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es : {indice} y el valor es: {valor}')


#usando el for/else
for numero in numeros:
    print(f'Ejecutando el utlimo bucle, valor actual: {numero}')
else:
    print('el bucle termino')



