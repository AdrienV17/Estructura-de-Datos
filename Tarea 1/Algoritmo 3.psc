Proceso Problema_3
	Definir horas como Entero
	Definir total Como Real
	
	Escribir '¿Cuántas horas duró?'
	leer horas
	
	Si horas<= 2
		total = horas*5
	FinSi
	Si horas>2 y horas<=5
		total = 10 + ((horas-2)*4)
	FinSi
	Si horas>5 y horas<=10
		total = 22 + ((horas-2)*3)
	FinSi
	Si horas>10
		total = 37 + ((horas-2)*2)
	FinSi		
	Escribir 'El total a pagar por su tiempo de ', horas, ' horas es de B/. ' total
FinProceso
