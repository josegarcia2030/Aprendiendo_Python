#PITAGORAS
#Escriba un programa que reciba como entrada las longitudes de
#los dos catetos "a" y "b" de un triangulo rectangulo, y que entregue
#como salida el largo de la hipotenusa "c" del triangulo, dado por
#el teorema de Pitagoras c**2 = a**2 + b**2




def pedirCateto():
    cateto = int(input("Escribe el cateto : \n"))
    return cateto

cateto_a = pedirCateto()
cateto_b = pedirCateto()


def teoremaPitagora(a,b):
    h = a**2 + b**2
    hipotenusa = h ** 0.5
    return hipotenusa

resultado = round(teoremaPitagora(cateto_a,cateto_b), 5)

print(f'El resultado es : {resultado}')