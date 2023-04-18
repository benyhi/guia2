#Dada una serie de números reales positivos, determinar el valor máximo y mostrarlo al final. 
#Se deberá ir preguntando si hay más números para ingresar.

maximo = 0
hayDatos = 0

while hayDatos != "si":
    numero = int(input("Ingrese un valor: "))
    if numero > maximo: 
        maximo = numero 
    hayDatos = input("Hay mas? Si/No: ")
print("El numero ingresado mas grande es", maximo)