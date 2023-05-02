from codecs import utf_8_encode


def MiFuncionSuma(A, B, C, imprime=True):
    resultado = A + B + C
    if imprime != False:
        print(resultado)
    return resultado


a = 4
variable_b = 5
var_c = 10

MiFuncionSuma(a, variable_b, var_c)



def mi_funcion_suma(a, b, c, imprime=True):
    resultado = a + b + c
    if imprime:
        print(resultado)
    return resultado

a = 4
variable_b = 5
varc_c = 10

mi_funcion_suma(a, variable_b, varc_c)


#1 espacios entre metodos
#2 espacios entre clases y funciones

class ClaseA:
    def metodo_a(self):
        pass

    def metodo_b(self):
        pass


class ClaseB:
    def metodo_a(self):
        pass

    def metodo_b(self):
        pass


def funcion():
    pass


def calcula_media_mediana(valores):
    #calculamos la media
    suma_valores = 0
    for valor in valores:
        suma_valores += valor
    media = suma_valores / len(valores)

    #Calculamos la mediana 
    valores_ordenados = sorted(valores)
    indice = len(valores) // 2
    if len(valores) % 2:
        mediana = valores_ordenados[indice]
    else:
        mediana = (valores_ordenados[indice] + valores_ordenados[indice + 1]) / 2
    
    return media, mediana

#Se nos recomienda usar espacio con operadores de asignacion

#correcto
x = 5

#incorrecto
x=5

#Y tambien con operadores relacionales

#correcto
if x == 5:
    pass

#incorrecto
if x==5:
    pass


#Pero cuando tengamos funciones con argumentos por defecto, no debemos dejar espacios

#correcto
def mi_funcion(parametro_por_defecto=5):
    print(parametro_por_defecto)

#incorrecto
def mi_funcion(parametro_por_defecto = 5):
    print(parametro_por_defecto)



#Por otro lado se recomienda "no dejar espacios dentro del parentesis"

def duplica(a):
    return a * 2

#correcto
duplica(2)

#incorrecto
duplica( 2 )


#Y tampoco entre "corchetes"

#correcto
lista = [1, 2, 3, 4]

#incorrecto
lista = [ 1, 2, 3, 4 ]


#No dejar espacios en potencia y en en parentesis

#correcto
y = x**2 + 1
z = (x-y) + (x+y)

#incorrecto
y = x ** 2  + 5
z = (x - y) * (x + y)



#Agrupar por orden de ejecucion

#correcto
if x > 0 and x % 2 == 0:
    print('.......')

#correcto
if x>0 and x%2==0:
    print('.......')

#incorrecto
if x% 2 == 0:
    print('.............')



#No usar espacios antes de "," en llamadas a funciones o metodos

#correcto
print(x, y)

#incorrecto
print(x , y)


#Cuando usemos listas no usar espacios antes del indice o entre el indice y los []

#correcto
lista[0]

#Incorrecto
lista [1]

#Incorrecto
lista[ 1 ]


#No alinear la variables

#correcto
var_a = 0
variable_b = 10
otra_variable_c = 3


#Incorrecto
var_a           = 0
variable_b      = 10
otra_variable_c = 3


a = "1234567891011121314151617181920212223242526272829303132333435363738394041424344"
#print(len(a))


#El tamaño de linea debe ser menor a 79 caracteres

#correcto
def mi_funcion(primer_parametro, segundo_parametro,
               tercer_parametro, cuarto_parametro,
               quinto_parametro):
    print('Python..!!')

#Incorrecto
def mi_funcion(first_paraments, seconds_paraments, three_paraments, four_paraments, five_paraments):
    print('Python...!!')

def mi_funcion(primer_paramtro, segundo_parametro,
    tercer_parametro, cuarto_parametro,
    quinto_parametro):
    print('Python...!!!!!')


#Analogamente podemos romper un "if" en diferentes lineas,util cuando se usan
#gran cantidad de condiciones que no entran en una sola linea

#correcto
condicion_A = 0
condicion_b = "0"

if (condicion_A and 
    condicion_b):
    print('Python...')



#En caso de romper una linea imposible de romper, usamos "\" para continuar
#en una nueva linea

#correcto
#with open('/esta/ruta/es/muy/pero/que/muy/larga/y/no/entra/en/una/sola/liena/') as fichero_1, \
    #open('/esta/ruta/es/muy/pero/que/muy/larga/y/no/entra/en/una/sola/liena/') as fichero_2:
    #fichero_2.write(fichero_1.read())



'''
Operaciones largas
Si queremos realizar una operación muy larga que no entra en una línea, 
tendremos que dividirla en múltiples. Lo recomendado es usar el operador
al principio de cada línea, ya que resulta mas fácil de leer.
'''

variable_a = 0
variable_b = ""
variable_c = 25
variable_d = 1
variable_d = 3
variable_f = 5
#Incorrecto
#income = (variable_a + variable_b + variable_c - variable_d - variable_f)


#Correcto

'''come = (variable_a
        + variable_b
        + variable_c
        + variable_d
        + variable_d
        + variable_f)'''

#coding: utf_8_encode

print("La acentuación del Español")




#Python define como nombrar a cada tipo de la siguiente manera :

#FUNCIONES: Letras en minusculas separadas por barra baja: 
#           funcion, mi_funcion, funcion_de_prueba

#VARIABLE: Al igual que las funciones:
#            variable, mi_variable, la_variable_extra

#CLASES: Uso del CamelCase, usando mayusculas y sin barra baja:
#            MiClase, LaClase, MiClaseDePrueba

#CONSTANTES: Nombrarlas usando mayusculas y separadas por barra baja
#           UNA_COONSTANTE, OTRA_CONSTANTE, MI_CONSTANTE_PI

#MODULO(ARCHIVOS .py): Igual que las funciones
#           modulo.py, mi_modulo.py, 

#PAQUETES(CARPETAS):    En minusculas pero sin separar por barra baja
#           packete, mipaquete



'''
EJEMPLO
'''

#mi_script.py

CONSTANTE_GLOBAL = 10

class MiClase():
    def mi_primer_metodo(self, variable_a, variable_b):
        return (variable_a + variable_b) / CONSTANTE_GLOBAL

    def segundo_metodo(self):
        pass


mi_objeto = MiClase()
print(mi_objeto.mi_primer_metodo(5,5))



