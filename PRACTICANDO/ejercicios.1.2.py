
#Escriba un programa que reciba como entrada el radio de un circulo y entregue 
#como salida su perimetro y su area..

#Para saber perimetro la formula es : 2 * PI * radio
#Para saber el area la formula es : PI * (radio * radio)



#variables
PI = 3.14

def pedirRadio():
    radio = float(input("Escribe el radio para calcular\n"))
    return radio

def saberPerimetro(radio):
    perimetro = (2 * PI * radio)
    return perimetro

def saberArea(radio):
    area = PI * (radio * radio)
    return area

def mostrar(perimetro, area):
    print(f'El Perimetro es : {perimetro}\nEl Area es : {area}')


radio = pedirRadio()
perimetro = saberPerimetro(radio)
area = saberArea(radio)

mostrar(perimetro,area)