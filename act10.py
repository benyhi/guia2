# Dada una lista de nombres y de salarios respectivos, determinar el salario mínimo y 
# mostrar el nombre de la persona que menos gana.

print('Ingrese la palabra STOP cuando desea finalizar')
terminar = 0 
minimo = 0 

while terminar != 'stop': 
    terminar = input('Ingresa tu nombre: ')
    salario = int(input('Ingresa tu sueldo: '))

    if minimo < salario: 
        minimo = salario 

        print('El salario mas bajo es de: ', minimo)
    
