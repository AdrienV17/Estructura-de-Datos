Proceso Problema_5
		Definir articulo como caracter
		Definir costo, descuento, total como real
		
		Escribir "Escriba el nombre del articulo"
		Leer articulo
		Escribir "Escriba el costo del articulo:"
		Leer costo
		
		Si costo>=200
			total = costo-(costo*0.15)
			Escribir "El articulo tendra un descuento de:" 15 "%"
			Escribir "el costo del articulo sera de:" total "dolares"
		Fin Si
		Si costo>100 y costo<200
			total = costo-(costo*0.12)
			Escribir "el articulo tendra un descuento de:" 12 "%"
			Escribir "el costo del articulo sera de:" total "dolares"
		Fin Si
		Si costo<100 
			total = costo-(costo*0.10)
			Escribir "el articulo tendra un descuento de:" 10 "%"
			Escribir "el costo del articulo sera de:" total "dolares"
		Fin Si
FinProceso
