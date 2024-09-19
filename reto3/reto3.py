"""
Julio Rocha
Liceth Rodriguez
Marcy Castro
"""

import math
#se le da la bienvenida al usuario
print ("ienvenido a la calculadora que te permitira conocer el volumen de la pelota segun el radio")
#Se le solicicta al usuario que ingrese el radio de la circunferencia o pelota
radio = float(input("ingresa el radio de la pelota o de la corcunferencia: "))
#Se utiliza la formula para conocer el volumen de la esfera concodiendo su radio
Vpelota = (4/3)*math.pi*(radio**3)
#se utliza la funcion round() para solo utilizar 
VRpelota = round (Vpelota,3)
#se le muestra al ususario el resultado de la operacion
print ("el volumen de la pelota es: ", VRpelota, "metros cubico")
print ("gracias por elegirnos, Feliz Dia") #Se despide al usuario