#encontrando el numero mayor de una lista
numeros = [4,7,1,42,15]
print(numeros)
numero_mas_alto = max(numeros)
print(f'El numero mayor es : {numero_mas_alto}')


#encontrando el numero menor de una lista
numero_menor = min(numeros)
print(f'El numero menor es : {numero_menor}')

#redondear a un numero entero sin decimales



numero_uno = 12.5154656
#redondeando a 4 decimales
print(numero_uno)
resultado = round(numero_uno, 4)
print(f'Numero redondeado a 4 decimales : {resultado}')



#retorna False -> 0, vacio, False, ninguno
resultado_bool = bool()
print(resultado_bool)

#retorna True -> distinto a 0 -> datos no vacios
resultado_bool = bool("yes")
print(resultado_bool) 


#retorna True, si todos los valores son verdaderos
resultado_all = all([2,"true",[344,25]])
print(resultado_all)



#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)