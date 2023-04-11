
nombre  = 'jose enrique'
apellido = 'garcia flores'
edad = 26
direccion = 'B/Olender avenida sudamerica'
estatura = 1.69
correo = "jose.garcia.f.2010@gmail.com"
trabaja = True


print(f'Bienvenido {nombre} {apellido}')

lista_compras = ["frutas", "leche", "carne", "pollo", "pan"]

if(not trabaja):
    print("Ten un buen dia en tu trabajo")
else:
    print("Reliza las compras de la lista")
    for lista in lista_compras:
        print(lista)


