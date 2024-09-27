Algoritmo paneles_solares
	eficienciaP = 0.15
	radiacionS=5
	apanel=1.6
	potencia_diaria=(apanel*radiacionS*eficienciaP)
	Escribir "la potencia diaria es: " potencia_diaria  " kWh"
	potencia_anual = potencia_diaria*365
	Escribir  "la potencia anual es: " potencia_anual " kWh"
	consumo1=  12000/potencia_anual
	nredondeado = REDON(consumo1) 
	Escribir "la cantidad que se necesita es " nredondeado " paneles solares para un consumo anual de 12000 kWh"
	Escribir "" //linea en blanco
	Imprimir "Extra"
	Escribir "" //linea en blanco
	definir eficienciaU, radiacionU, tamañoU, horasU, consumoU, potenciaU como real 
	Escribir "Ingresa la eficiencia del panel solar en decimal: "
	leer eficienciaU
	Escribir "Ingresa la radiacion solar en metros cuadrados del panel solar: "
	leer radiacionU
	Escribir "Ingrese el tamaño del panel solar: "
	leer tamañoU
	Escribir "Ingresa las horas del uso del panel solar: "
	leer horasU
	potenciaA= (eficienciaU*radiacionU*tamañoU)*365
	Escribir "La potencia anual es: " potenciaA
	Escribir "Ingresa el consumo anual: "
	leer consumoU
	Escribir "Ingresa la potencia anual: "
	leer potenciaU
	panel1 = consumoU/potenciaU
	rpanel = REDON(panel1)
	Escribir "Se necesita una cantidad de: " rpanel " paneles solares para un consumo anual de: " consumoU "kWh"
	AreaTo = rpanel*apanel
	Escribir "Se necesita un area de: " AreaTo "metros cuadrados."
FinAlgoritmo
