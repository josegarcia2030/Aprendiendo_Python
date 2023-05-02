#
# VARIABLES
#

'''
Entre las variables que utilizaremos en python estan
    - string
    - int
    - float
    - boleanos
'''
def init():

    nombre = "jose enrique"
    apellido = "garcia flores"
    edad = 25
    estudia = False
    trabaja = True
    sueldo = 2552.69
    descripcion = "Soy un joven de 25 años, que estudia en el area de IT"

    def mostrar_info():
        name = nombre.upper()
        lastname = apellido.upper()
        info = f'{name} {lastname} de {edad} años'
        print(info)




    def el_trabaja(desc):
        res = ("trabaja" in desc)
        if res:
            print('Es un joven trabajador')
        else:
            if ("estudia" in desc):
                print("Es un joven que estudia")

    #mostrar_info()
    #el_trabaja(descripcion)





    #
    #  OPERADORES DE COMPARACION
    #

    '''
    == ES IGUAL QUE
    != ES DISTINTO DE
    < ES MENOR QUE
    <= ES MENOR O IGUAL QUE
    > ES MAYOR QUE
    >= ES MAYOR O IGUAL QUE
    '''

    def poder_tomar(edad, name):
        if edad >= 18:
            aviso = f'Debido a que tienes {edad} años\nYa puedes tomar {name}'
            print(aviso)
        else:
            aviso = f'Debido a que tienes {edad} años\nNo puedes tomar {name}'

    
        
    
    def alquiler_depa(sueldo,precio_alquiler):
        para_alquiler = round(sueldo / 2, 2)
        if para_alquiler >= precio_alquiler:
            aviso = f'Debido a que dispones de {para_alquiler}Bs para alquiler, puedes alquilarlo'
            print(f'El alquiler es {precio_alquiler}')
            print(aviso)
        else:
            aviso = f'Debido a que dispones de {para_alquiler}Bs, No puedes Alquilar'
            print(f'Precio del aquiler {precio_alquiler}')
            print(aviso)

    #poder_tomar(edad, nombre)
    #alquiler_depa(sueldo, 1200)

    def calcular_gastos_almuerzo(almuerzo):
        gasto_mensual = almuerzo * 30
        return round(gasto_mensual, 2)

    def calcular_gastos_desayuno(desayuno):
        gasto_mensual = desayuno * 30
        return round(gasto_mensual, 2)
    
    def calcular_gastos_cena(cena):
        gasto_mensual = cena * 30
        return round(gasto_mensual)
    
    def calcular_gastos_comida(desayuno, almuerzo, cena):
        gasto = desayuno + almuerzo + cena
        info_gastos = f'Tus gastos son de {gasto}Bs al mes en comidas'
        print(info_gastos)

    desayuno_mes = calcular_gastos_desayuno(7)
    almuerzo_mes = calcular_gastos_almuerzo(13)
    cena_mes = calcular_gastos_cena(13)


    #calcular_gastos_comida(desayuno_mes, almuerzo_mes, cena_mes)

    def pedir_numero_uno():
        numero = int(input('Escribe el 1er numero de la Operacion\n'))
        return numero
    
    def pedir_numero_dos():
        numero = int(input('Escribe el 2do Numero para la Operacion\n'))
        return numero
    
    def operacion_aritmetica():
        
        opcion = int(input('Elige la opcion que te guste\n'
                       + '1.- Potenciacion\n' 
                       + '2.- Division Baja\n'
                       + '3.- Resto o Modulo\n'))
        
        num_uno = pedir_numero_uno()
        num_dos = pedir_numero_dos()

        if opcion == 1:
            print('Has elegido la opcion de Potenciacion\n')
            resultado = num_uno ** num_dos
        elif opcion == 2:
            print('Has elegido la opcion de Division Baja\n')
            resultado = num_uno // num_dos
        elif opcion == 3:
            print(f'Has elegido Resto - Modulo')
            resultado = num_uno % num_dos
        else:
            print(f'No has elegido ninguna de las opciones')

        aviso = f'El resultado de la operacion es {resultado}'
        print(aviso)

    #operacion_aritmetica()


    def operacion_logicos():
        #
        if trabaja | estudia:
            print('Vives sin tus padres?')


        if trabaja & (sueldo > 2000):
            print('Estas estudiando?')

        if not estudia:
            print('estudiando sistemas')
        else:
            print('Dejaste la U')    

        if not trabaja:
            print('Dejaste tu trabajo?')
        else:
            print('En que trabajas?')



    #operacion_logicos()


    '''
    DATOS COMPUESTOS
    '''

    #1.- Una Lista es una Matriz
    lista_compras_mercado = ["azucar", "carne", "aceite", "cafe"]
    indice = 0
    print(f'Lista de compras')

    for l in lista_compras_mercado:
        indice += 1 
        print(f'{indice}.- {l}')


    #2.- Las Tuplas == Nose pueden Modificar












init()



