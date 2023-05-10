#DETERMINAR PAR

'''
Escriba un programa que determine si el numero entero ingresado
Por el usuario es par o no.
'''



'''def averiguar_es_par():
    pregunta = int(input("1.- Ingresar\n2.- Salir"))
    if pregunta == 1:
        preguntar = True
        while preguntar:            
            try:
                numero = int(input("Escribe el numero que quieres saber si es par o no\n"))
                print(f'Escribiste este numero {numero}')

            except:
                print("Escribe un numero\n")
    else:
        pass
        '''

'''numero = int(input("Escribe el numero que quieres saber si es par\n"))

if numero % 2 == 0:
    print(f'El numero {numero} es PAR')
else:
    print(f'El numero {numero} es IMPAR')'''


    
try:
    while True:
        numero = int(input("Escribe un numero disinto a 0 - Escribe 0 para salir\n"))
        if numero != 0:
            if numero % 2 == 0:
                print(f'Es PAR')
            else:
                print(f'Es IMPAR')
        else:
            print(f'Saliste del Programa')
            break 
except ValueError as e:
    print("Escribe un numero\n")
    print(f'ERROR {e}')