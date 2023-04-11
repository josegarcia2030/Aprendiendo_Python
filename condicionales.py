#Condcionales

'''
si condicion se cumple :
    #codigo a ejecutar
de lo contario:
    #se ejecuta este codigo
'''

edad = 17

if edad >= 18:
    print("podes pasar")
else:
    print("no podes pasar")
    
print("Disfruta tu dia..!!!")


password = "rasek2030"
contrasena = "rasek2030"

if(contrasena == password):
    print("Inicia session")
else:
    print("contraseña incorrecta")
    
    
    
ingreso_mensual = 1000000

if ingreso_mensual > 1000:
    print("esa bien tu ingreso economico en latinoamerica")
if ingreso_mensual > 10000:
    print("estas bien en cualquier parte del mundo")
else:
    print("sos pobre")
    
    
ingreso_anual = 120

if ingreso_anual > 100000:
    print("estas bien en cualquier pais")
elif ingreso_anual > 1000:
    print("estas bien en latinoamerica")
elif ingreso_anual > 500:
    print("estas bien en argentina")
else:
    print("Sos pobre")
    
gastos_mensuales = 5000

if ingreso_mensual > gastos_mensuales:
    print("estas utilizando bien tu dinero")