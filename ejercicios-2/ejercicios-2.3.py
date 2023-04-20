
#creando una funcion que muestre la serie fibonnaci entre 0 y el numero dado


def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num:
            return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a,b = b, a + b



resultado = fibonacci(34)
print(resultado)




primos_hasta = lambda num : list(filter(lambda x : all(x % i !=0 for i in range(2, int(x ** 0.5) + 1)), range(2, num)))
print(primos_hasta(15))




