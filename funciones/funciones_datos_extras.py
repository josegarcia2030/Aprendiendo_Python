#creando una funcion de 3 parametros
def frase(nombre,apellido, adjetivo):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frease_resultante = frase("jose", "garcia", "valiente")


#utilizando keywords arguments
def frase_dos(apodo ,argu = "sonso"):
    return f'{apodo}, sos muy  {argu}'

frase_nueva = frase_dos("rasek2030")
print(frase_nueva)