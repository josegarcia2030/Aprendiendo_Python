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



    #BUCLES
    def mi_bucle():
        cont = 0
        while cont < 10:
            cont += 1
            print((cont))
            
    def crear_mi_bucle():
        cont = 0
        lista = []
        cantidad = int(input\
            ('Escribe la cantidad de veces que pondras las notas\n'))
        
        while cont < cantidad:
            cont += 1
            dato = input('Escribe la nota\n')
            lista.append(dato)

        print(lista)

    #crear 2 listas
    lista_1 = ['enrique','jose','miguel','luis']
    lista_2 = ['69246604','77814106','78136195','65041514']

    for l_1, l_2 in zip(lista_1, lista_2):
        print(f'Nombre : {l_1}\nCelular: {l_2}')
            #pass 

    def recorrer_dos_listas(list_1, list_2):   
        pass


    lista_a = [1, 2, 3]
    lista_b = [4, 5, 6]


    for tupla in zip(lista_a, lista_b): #obtenemos la tupla en cada iteración
        print(tupla[0], tupla[1])

    for valor_a, valor_b in zip(lista_a, lista_b): #obtenemos los valores en cada iteración
        print(valor_a, valor_b)

    recorrer_dos_listas(lista_1, lista_2)    
    #crear_mi_bucle()
    #mi_bucle()














    '''
    DATOS COMPUESTOS
    '''

    #1.- Una Lista es una Matriz
    lista_compras_mercado = ["azucar", "carne", "aceite", "cafe"]
    indice = 0

    #print(f'Lista de compras')
    '''for l in lista_compras_mercado:
        indice += 1 
        print(f'{indice}.- {l}')'''


    #2.- Las Tuplas == Nose pueden Modificar
    usuarios = ("rasek2030","peji7","rxH27","mauro27")
    


    def mostrar_mi_lista(lista):
        indice = 0
        print("Esta es la lista:\n")
        for l in lista:
            indice +=1
            print(f'{indice}.- {l}')

    #mostrar_mi_lista(lista_compras_mercado)


    #3.- Conjunto(Set)
    #No se puede cambiar los elementos del conjunto
    #No se puede acceder por indice[i]
    #No almacena datos duplicados

    mi_conjunto = {"ingeniero de sistemas","abogado","doctor","arquitecto"}
    #mostrar conjunto
    #print(mi_conjunto)


    #4.- DICCIONARIO
    #key : value
    #clave : valor

    mi_diccionario = {
        'nombres': 'jose enrique',
        'apellidos': 'garcia flores',
        'edad': 26,
        'estudia': False,
        'trabaja': True,
        'sueldo': 3562.63
    }

    nombre = mi_diccionario['nombres'].upper()
    #print(f'El nombre es {nombre}')




    #DESEMPAQUETADO
    #TUPLA usuarios

    usuario_1, usuario_2, usuario_3, usuario_4 = usuarios

    def mostrar_dempaquetado():
        print(usuario_1)
        print(usuario_2)
        print(usuario_3)
        print(usuario_4)    



    #mostrar_dempaquetado()



    #crear lista
    contactos = ["jose","enrique","luis","miguel","mauricio","moy"]
    cant = len(contactos)
    num = 0
    mis_contactos = []

    for c in contactos:
        num += 1
        palabra = "contactos_"
        palabra += str(num)
        mis_contactos.append(palabra)

    #print(mis_contactos)


    #crear una tupla con tuple()
    tupla = tuple(['dato1','dato2','dato3'])
    
    def mostrar_tupla(tupla):
        for t in tupla:
            print(t)


    #mostrar_tupla(tupla)

    #Crear una lista con list()
    lista = list(['name1','name2','name2',2030])
    def mostrar_lista(lista):
        for l in lista:
            print(l)

    #mostrar_lista(lista)


    #DICCIONARIOS con DICT()
    diccionario = dict(nombre = 'enrique', apellido = 'garcia', edad = 26)
     
    mis_contactos = dict(contacto_1 = "69246604", contacto_2 = "77814106")


    #Crear Tupla con Tuple()
    mi_tupla = tuple(['dato1', 'dato2','dato3','dato4','dato5'])

    print(mi_tupla)












init()



