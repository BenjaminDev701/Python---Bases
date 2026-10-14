# args: captura cualquier cantidad de argumentos que se pasen por posicion (Tupla = separadas por ',')
# kwargs: captura cualquier cantidad de argumentos que se pasen por palabra clave (Diccionario = separadas por '=', ejemplo: clave=valor)

def big_fuction(*args, **kwargs):
    print(args)
    print(kwargs)

    return args


print(big_fuction(1, 2, 3, 4, 5, 6, 7, num1=3, num2=6))
