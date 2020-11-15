Proceso Problema_1
	// Variables a necesitar
	Definir sueldo,horas,pago_por_hora Como Real
	Definir excedente Como Real
	
	//Recoleccion de datos
	Escribir 'Bienvenido a este programa!'
	Escribir 'Ingrese las horas trabajadas'
	leer horas
	
	Escribir 'Ingrese el pago por hora'
	leer pago_por_hora
	
	//Ejecucion de calculo
	excedente = horas - 40
	sueldo = pago_por_hora * horas
	Si excedente>0
		sueldo = sueldo + (excedente*(pago_por_hora*2))
	FinSi
	//Impresion en pantalla final
	escribir 'El sueldo del trabajador en base a ',horas,' horas trabajadas y un salario de B/. ',pago_por_hora,' por hora es de: '
	escribir 'B/. ',sueldo
	
	
FinProceso
