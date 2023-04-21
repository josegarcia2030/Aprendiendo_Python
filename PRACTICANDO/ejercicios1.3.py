
#Escriba un programa que calcule el promedio de 4 notas
#ingresadas por el usuario


def saberPromedio():
    nota_uno = 0
    nota_dos = 0
    nota_tres = 0
    nota_cuatro = 0
    promedio = 0


    nota_uno = int(input("Escribe la nota 1 : \n"))
    nota_dos = int(input("Escribe la nota 2 : \n"))
    nota_tres = int(input("Escribe la nota 3 : \n"))
    nota_cuatro = int(input("Escribe la nota 4 : \n"))

    promedio = (nota_uno + nota_dos + nota_tres + nota_cuatro) / 4

    print(f'El promedio es : {promedio}')



notas = []

def pedirNotas():
    for i in range(4):
        nota = int(input("Escriba la nota: \n"))
        notas.append(nota)


def mostrarNotas():
    for n in notas:
        print(n)


def elPromedio():
    promedio = 0
    for n in notas:
        promedio += n
    
    num = len(notas)
    promedio = promedio / num
    return promedio



pedirNotas()
print(elPromedio())