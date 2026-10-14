# args: captura cualquier cantidad de argumentos que se pasen por posicion (Tupla = separadas por ',')
# kwargs: captura cualquier cantidad de argumentos que se pasen por palabra clave (Diccionario = separadas por '=', ejemplo: clave=valor)

def bif_fuction(*args, **kwargs):
    print(args)
    print(kwargs)
