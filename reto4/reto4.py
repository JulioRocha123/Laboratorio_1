"""
Julio Rocha
Liceth Rodriguez
Marcy Castro
"""
#Se le solicta al usuario que ingrese los datos
nivel = int(input("Ingresa tu nivel de acceso: "))
cambio = input("Su contraseña fue cambiada en un plazo de 30 dias? Si | No ")
tarjeta = input("Su tarjeta se encuentra activa? Si | No ")
#se recisa que el nicel de acceso sea necesario
if nivel >= 1 and nivel <= 5:
        #Se verifica que el usuario tenga la tarjeta activa
        if tarjeta == "Si":
            # se verifica que el ususario haya cambiado la contraseña en periodo de 30 dias
            if cambio == "Si":
                #se le da acceso al ususario con todas las verificaciones 
                print ("Acceso permitido")
            else:
                print ("Acceso denegado: Debe cambiar la contraseña.")
        else:
            print ("Acceso denegado: Tarjeta inactiva.")
else:
        print ("Acceso denegado: Nivel de acceso insuficiente.")