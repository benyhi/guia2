#Pedir los montos de sueldos de los empleados de una empresa hasta que no haya más y mostrar el total.
 
total = 0 
for i in range (3):
    salary = int(input("Salario: "))
    total = total + salary

print ("El total del monto es", total)