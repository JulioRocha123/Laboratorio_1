"""
Julio Rocha
Liceth Rodriguez
Marcy Castro
"""
import math
radio = float(input("ingresa el radio de la pelota o de la corcunferencia: "))
Vpelota = (4/3)*math.pi*(radio**3)
VRpelota = round (Vpelota,3)
print ("el volumen de la pelota es: ", VRpelota, "metros cubico")