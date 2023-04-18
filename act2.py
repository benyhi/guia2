#Preguntar si hay datos para ingresar, en caso afirmativo solicitar un número entero 
#y decir si es negativo o no. Preguntar si repite.

hayDatos = input("Hay algun dato para ingresar?: ")
while hayDatos == "si":
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    if numero >= 0:
        print("El numero", numero,"no es negativo")
    else:
        print("El numero", numero,"es negativo")
        hayDatos = input("Hay algun dato para ingresar: ")



    


