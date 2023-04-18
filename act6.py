#Preguntar cuántas personas se van a cargar y luego solicitar sus edades, mostrando al final la edad promedio.

valorf = int(input('Ingresa la cantidad de personas que deseas promediar: ' ))
promedio = 0 

for i in range (valorf):
    print("Ingresa la edad de la persona n°", i+1)
    edad  = int(input())
    promedio = promedio + edad 

print ("Tu promedio es: ", promedio/valorf)