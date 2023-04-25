#Hora futura
#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora #marcará el reloj dentro de h horas:


#Hora actual: 3
#Cantidad de horas: 5
#En 5 horas, el reloj marcara las 8


#Hora actual: 11
#Cantidad de horas: 43
#En 43 horas, el reloj marcara las 6


hora = int(input("Escribe la hora actual...\n"))
cant_horas = int(input("Escribe la Cantidad de Horas que van a trascurrir...\n"))
t = ""



#print(f'Son las {hora}{t}')
cont = 0
while cont < cant_horas:
    hora += 1
    if hora > 23:
        hora = 0
    cont += 1

if hora > 0 and hora < 13:
    t = "am"
elif hora > 12 and hora <= 23:
    t = "pm"


print(f'La hora sera {hora}{t}')





























