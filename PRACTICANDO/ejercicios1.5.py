#NUMERO INVERTIDO
#Escriba un programa que pida al usuario un entero de tres digitos,
#y entregue el numero con los dos digitos en orden inverso


num = input("Escribe un numero:\n")
numero = []
nuevo_numero = ""

def agregarAlista():
    for n in num:
        valor = n
        numero.append(valor)

def invertirLista():
    numero.reverse()

def asignar():
    num = ""
    for n in numero:
        num += n
    return num

agregarAlista()
invertirLista()
nuevo_numero = asignar()
print(nuevo_numero)




