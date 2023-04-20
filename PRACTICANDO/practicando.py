#Tipo de Datos Simples

#variables
nombre = "jose enrique"
apellido = "garcia flores"
edad = 26
puesto_trabajo = "Ingeniero - Sistemas"
sueldo = 7824.69
descripcion = "El trabajador cuenta con una excelente salud, el unico inconveniente que se le observa, es que llega a tner una alergia a cierto medicamento 'Penisilina' "

def calcular_trabajo_dia(salario, dias):
    dia_trabajado = salario / dias
    return dia_trabajado


def mostrarDatosTrabajador(nombre, apellido, edad, puesto, sueldo):
    la_edad = str(edad)
    su_sueldo = str(sueldo)
    datos = f'Datos del Trabajador\nNombre Completo : {nombre} {apellido}\nEdad : {la_edad} años\nPuesto : {puesto}\nSueldo : {su_sueldo}Bs.\n'
    return datos


dia_trabajado = calcular_trabajo_dia(sueldo, 30)
#print(f'Al señor {nombre} {apellido}, se le paga x dia la suma de : {dia_trabajado}Bs.')
#print(mostrarDatosTrabajador(nombre,apellido, edad, puesto_trabajo, sueldo))

def esAlergico(texto):
    if "alergia" in texto:
        return "Es alergico"
    else:
        return "No es alergico"

#print(esAlergico(descripcion))

def descuento_aportes(sueldo):
    #Tasa de porcentaje de descuento es 12.71
    descuento = (sueldo * 12.71) / 100
    total = sueldo - descuento
    return total

sueldo_neto = descuento_aportes(sueldo)
#print(f'Total sueldo: {sueldo}Bs.\nTotal a pagar {sueldo_neto}Bs.') 



asistencia = []
horario_entrada = []
dias_laborales = 5
contador = 0



while contador < dias_laborales:
    dato = int(input('Digita la opcion correcta\n1.- Asistio\n2.- No llego\n'))
    
    if dato == 1:
        hora = input('Escribe la hora de llegada:\n')
        horario_entrada.append(hora)
    elif dato == 2:
        horario_entrada.append("0")
         
    asistencia.append(dato)   
    contador += 1

#print(asistencia)

vino = 0
no_vino = 0

for a in asistencia:
    if a == 1:
        vino += 1
    elif a == 2:
        no_vino += 1

#print(f'La cantidad de veces que asistio: {vino}')
#print(f'La cantidad de faltas que tuvo: {no_vino}')
#print(horario_entrada)
