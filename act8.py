#Ingresar autos y sus precios y contar cuantos valen entre $3.460.000 y $12.850.000.
#Terminar la carga cuando el valor ingresado sea 0.

precio = 1

print ("Cargue 0 cuando desea terminar")
while precio != 0:
    auto = input("Ingrese un modelo de auto: ")
    precio = int(input("Ingrese el precio del auto: "))

    if 3460000 < precio > 12850000: 
        precio =  precio + 1 
        
print('Cantidad de autos dentro del rango: ', precio)
