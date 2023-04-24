# Ingresar 7 números enteros y en el caso de que sean naturales de una sola cifra mostrar un cartel por cada uno.

for i in range (7): 
    numero = int(input('Ingresa un numero: '))

    if numero < 9: 
        print('Es de una sola cifra')

        