
nombre  = 'jose enrique'
apellido = 'garcia flores'
edad = 26
direccion = 'B/Olender avenida sudamerica'
estatura = 1.69
correo = "jose.garcia.f.2010@gmail.com"
trabaja = True

mis_datos_lista = [nombre, apellido, edad, direccion, estatura, correo, trabaja]
mis_datos_tupla = (nombre, apellido, edad, direccion, estatura, correo, trabaja)
mis_datos_conjunto_set = {nombre, apellido, edad, direccion, estatura, correo, trabaja}
mis_datos_diccionario = {
    'nombre': nombre,
    'apellido': apellido,
    'edad': edad,
    'direccion': direccion,
    'estatura': estatura,
    'correo': correo,
    'Trabaja' : trabaja
}

#print(f'Bienvenido {nombre} {apellido}')

lista_compras = ["frutas", "leche", "carne", "pollo", "pan"]

'''
if(not trabaja):
    #print("Ten un buen dia en tu trabajo")
else:
    #print("Reliza las compras de la lista")
    for lista in lista_compras:
        #print(lista)
'''

los_datos = f'La direccion de {nombre} {apellido} es : \n{direccion}\ny su estatura es : {estatura}cm'

#print(datos)

sueldo = 2200
pasaje_mensual = 30 * 8
desayuno = 30 * 7
almuerzo_mensual = 15 * 30
cena_mensual = 15 * 30
fin_de_semana = 4 * 150 

calcular_gastos = pasaje_mensual + desayuno + almuerzo_mensual + cena_mensual + fin_de_semana
#print(f"Los gastos de : {nombre} {apellido} son : {calcular_gastos}bs")
restante = sueldo - calcular_gastos
#print(f"Lo que le queda para ahorro es : {restante}bs")
sin_salir = fin_de_semana
#print(f"Se ahorraria {sin_salir}bs , si el no gastara cada fin de semana en salidas..")

if sueldo > calcular_gastos:
    if sueldo - calcular_gastos > 200:
        #print(f"{nombre} {apellido} estaras llegando a fin de mes con mas de : 200bs")
        ""
else:
    #print(f"{nombre} {apellido} tus gastos son mayores a lo que generas mensual..")
    ""
    
for mi_datos in mis_datos_lista:
    print(mi_datos)
    

    