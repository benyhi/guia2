#Pedir el ingreso de 5 números. Contar los mayores de 23. Mostrar el resultado.

confirmacion = input("Desea comprobar su numero escriba su opcion (SI) (NO): ")

confirmacion2 = ""
while confirmacion != "no": 

    if confirmacion == "si": 
        numero = int(input("Ingrese un numero real para la comprobacion: "))
           
        if numero < 0: 
            print('Su numero es negativo')
        else:
            print('Su numero no es negativo')
    else: 
        print("No hay problema vuelva pronto..")


        
    confirmacion2 = input('Desea hacer otra comprobacion, escriba su opcion (SI) (NO): ')
