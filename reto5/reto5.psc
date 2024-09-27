Algoritmo tienda_en_linea
		Definir dinero Como Real
		Definir cliente, codigo Como Caracter
		
		Escribir "Bienvenido a la supermacia"
		descuento <- 0 
		
		Escribir "Ingrese el valor del cliente: "
		Leer dinero
		Escribir "El cliente es VIP (SI | NO): "
		Leer cliente
		Escribir "El cliente tiene codigo especial (SI | NO): "
		Leer codigo
		
		Si dinero >= 100 Entonces
			descuento <- descuento + 0.2
		Fin Si
		
		Si cliente = "SI" Entonces
			descuento <- descuento + 0.1
		Fin Si
		
		Si codigo = "SI" Entonces
			descuento <- descuento + 0.05
		Fin Si
		
		total <- dinero * (1 - descuento)
		
		total <- Redon(total)
		Escribir "El precio total a pagar es de: ", total, "$"
		Escribir "Adios, Gracias por elegirnos"
	Fin Proceso
