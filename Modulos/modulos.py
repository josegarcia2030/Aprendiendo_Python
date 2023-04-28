from modulo_saludar import saludar as saludo
import modulo_operaciones_aritmeticas as op_aritmeticas
from modulo_prueba import sueldoNeto, descuento


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


operacionSueldo()





