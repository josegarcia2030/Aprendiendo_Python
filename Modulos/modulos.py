from modulo_saludar import saludar as saludo
import modulo_operaciones_aritmeticas as op_aritmeticas
from modulo_prueba import sueldoNeto, descuento
from funciones_buenas.funciones import calcular_sueldo_dia as calcular_dia
import sys
sys.path.append("c:\\Users\\kiwi\\Documents\\Aprendiendo_Python\\funciones")
import parametros_args as modulo_suma
#import crear_funciones as mis_funciones
#sys.path.append("c:\\Users\\kiwi\\Documents\\Aprendiendo_Python\\bucles")
#import mas_iteraciones as iteracion



#Metodo del modulo_saludar
def saludos():
    saludos = saludo("Rasek2030")
    print(saludos)

#Metodo del modulo_operaciones_aritmeticas
def operacionSuma():
    num1 = int(input("Escribe el 1 numero para la sumna\n"))
    num2 = int(input("Escribe el 2 numero para la suma\n"))
    resultado = op_aritmeticas.suma(num1, num2)
    print(f'La suma de {num1} + {num2} es : {resultado}')


#saludos()
#operacionSuma()

def operacionSueldo():
    sueldo = float(input("Escribe tu sueldo sin descuento..\n"))

    desc = round(descuento(sueldo),2)
    sueldo_neto = sueldoNeto(sueldo,desc)

    print(f'Tu descuento sera de : {desc}BS.\n')
    print(f'Se te pagara {sueldo_neto}BS.\n')


def mostrar_Par_Impar(boleano):
    if boleano:
        print(f'El numero es Par')
    else:
        print(f'El numero es Impar')




#operacionSueldo()


#print('El dia trabajado sera de : ' + str(calcular_dia(7500,30)))
#print(sys.path)



modulo_suma.sumar(1034,45)

#mis_funciones.saludar()


'''usuarios = ["rasek2030","rxH","Alarito", "mauroRX", "peji7"]
iteracion.bucle(usuarios)'''
