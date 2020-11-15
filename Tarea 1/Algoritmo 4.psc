Proceso Problema_4
	Definir nombre1, nombre2, nombre3 como cadena;
	Definir edad1, edad2, edad3 como entero;
	
	Escribir "Persona 1"
	Escribir "¿Cual es tu nombre?"
	Leer nombre1;
	Escribir "¿Cuantos años tienes?"
	Leer edad1;
	Escribir "Persona 2"
	Escribir "¿Cual es tu nombre?"
	Leer nombre2;
	Escribir "¿Cuantos años tienes?"
	Leer edad2;
	Escribir "Persona 3"
	Escribir "¿Cual es tu nombre?"
	Leer nombre3;
	Escribir "¿Cuantos años tienes?"
	Leer edad3;
	si edad1 < edad2 
		si edad1<edad3 
			Escribir "La edad menor es de:",nombre1 
			Escribir edad1, "años"
		Sino
			Escribir "La edad menor es de: ",nombre3 
			Escribir edad3,"años"
		Finsi
	Sino
		si edad2 < edad3 
			Escribir "La edad menor es de: ",nombre2 
			Escribir edad2, "años"
		Sino
			Escribir "La edad menor es de: ",nombre3 
			Escribir edad3, "años"
             FinSi
       FinSi
FinProceso
