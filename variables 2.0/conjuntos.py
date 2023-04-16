#creando un conjunto con set()
conjunto = set(["dato1","dato2"])
print(conjunto)

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)


#teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {2,4,6,8}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
#print(resultado)

resultado = conjunto2 <= conjunto1
#print(resultado)


"verificar si es un superconjunto"
resultado = conjunto2.issuperset(conjunto1)
print(resultado)
resultado = conjunto1 > conjunto2
print(resultado)


#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

if resultado == False:
    print("Los conjuntos son igual")
else:
    print("Los conjuntos no son iguales")





