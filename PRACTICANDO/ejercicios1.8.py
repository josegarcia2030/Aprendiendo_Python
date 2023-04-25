#Parte decimal
#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

#Ingrese un numero: 4.5
#0.5
#Ingrese un numero: -1.19
#0.19




numero = input("Escribe un numero con 2 decimal\n")


if numero.count("."):
    decimal = numero.split(".")
    decimal.pop(0)
    #nuevo_numero
    nuevo_numero = float(decimal[0])
    if nuevo_numero < 10:
        nuevo_numero /= 10
    else:
        nuevo_numero /= 100
    print(f"Decimal es {nuevo_numero}")
else:
    print("No tiene parte decimal")    

























