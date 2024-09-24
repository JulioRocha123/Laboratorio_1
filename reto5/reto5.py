"""
Julio Rocha
Liceth Rodriguez
Marcy Castro
"""
#Se le da la bienvenida al ususario
print ("Bienvenido a la supermacia")
descuento = 0 #se establece el valor del descuento como 0
#se le pide al ususario que ingrese los datos del dinero, cliente, codigo
dinero = float(input("Ingrese el valor del cliente: "))
cliente = str(input("El cliente es VIP SI | NO: "))
codigo = str(input("El cliente tiene codigo especial SI | NO: "))
#si el dinero es mayor o igual a 100 se añade 0.2 al valor del descuento
if dinero >= 100:
    descuento =+ 0.2
#si el cliente es VIP se añade 0.1 al valor del descuento
if cliente == "si":
    descuento += 0.1
#si el cliente tiene un codigo de descuento se añade 0.05 al valor del descuento
if codigo == "si":
    descuento += 0.05
#se realiza la operacion para determinar el precio total a pagar añadiendole
#los descuentos establecidos
total = dinero * (1 - descuento)
total = round (total,2) #se redondea el numero para que el valor a pagar no sea tan extenso
#se le muestra al ususario el precio que debe pagar y asi mismo se despide
print ("El precio total a pagar es de:", total,"$ \nAdios, Gracias por elegirnos")