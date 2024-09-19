"""
Julio Rocha
Liceth Rodriguez
Marcy Castro
"""
#Imoortamos la libreria math
import math
#se le da la bienvenida al usuario
print ("Bienvenido a la calculadora que te permitira conocer el porcentaje de retrasos de tus empleados")
#Se le solicicta al usuario que ingrese los dias de retraso del proyecto
Dretraso = int(input("Ingresa los dias de retraso del proyecto: "))
#Se le solicicta al usuario que ingrese los dias asignados al proyecto
Dasignados = int(input("Ingresa los dias asignados al proyecto: "))
#Se utiliza la formula para conocer el oorcentaje de retraso
Pretraso = (Dretraso/Dasignados) * 100
#Se utiliza la funcion math.ceil para aproximar el numero a un numero mayor 
RPretraso = math.ceil(Pretraso)
#se le muestra al ususario el resultado de la operacion
print ("el porcentaje de restraso es del: ", RPretraso,"%") 
print ("gracias por elegirnos, Feliz Dia") #Se despide al usuario