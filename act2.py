#Preguntar si hay datos para ingresar, en caso afirmativo solicitar un número entero 
#y decir si es negativo o no. Preguntar si repite.

confirmacion = input("Desea comprobar su numero escriba su opcion (SI) (NO): ")

confirmacion2 = ""
while confirmacion != "no": 

    if confirmacion2 == "si": 
        numero = int(input("Ingrese un numero real para la comprobacion: "))
           
        if numero > 0: 
            print('Su numero es positivo')
        else:
            print('Su numero es negativo')
    else: 
        print("No hay problema vuelva pronto..")


        
    confirmacion2 = input('Desea hacer otra comprobacion, escriba su opcion (SI) (NO): ')



    


