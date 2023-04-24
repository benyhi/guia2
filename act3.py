#Pedir el ingreso de 5 números. Contar los mayores de 23. Mostrar el resultado.
print("A continuacion ingrese 5 numeros reales.")

contador = 0
for i in range(5):
    numero = int(input('Ingresa un numero: '))
    if numero > 23:
        contador = + 1 # counter = counter + 1
print('La cantidad de numeros mayores a 23 es:', contador)

