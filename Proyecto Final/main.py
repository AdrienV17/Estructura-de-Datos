# # Confeccione un programa que haga uso de apuntadores, estructuras dinámicas, 
# estructuras selectivas y repetitivas para desarrollar el siguiente Menú.   
# Menú Principal
# 1.	Pilas
# 2.	Colas
# 3.	Arboles Binarios
# 4.	Listas Enlazadas
# 5.	Grafos
# 6.	Salida

 
# Por Opción 1 (Pilas)
# 1.	 Insertar 
# 2.	Extraer 
# 3.	Visualizar
# 4.	Salida
# Por Opción 2 (Colas)
# 1.	Insertar
# 2.	Extraer
# 3.	Visualizar
# 4.	Salida
 

# Por Opción 3            				Por Opción 4
# 1.	Crear árbol					1. Crear la Lista
# 2.	Recorrido Preorden			2. Introducir elementos 
# 3.	Recorrido Post orden			3. Eliminar Elemento
# 4.	Recorrido Enorden			4. Recorrer la lista
# 5.	Salida						5. Salida

# Indicaciones
# Trabaje con Datos de tipo alfanumérico para cada una de las estructuras señalas. 
# El uso de apuntadores será valorado en la creación de la estructura. Documente su programa, 
# haga uso de funciones y estructura selectiva y repetitiva
from assets import menu_principal,opcion_pilas_colas,opcion_arboles,opcion_lista
from funciones import desplegar_lista,cargar,pausar,limpiar_pantalla
from ask import askInt
if __name__ == "__main__":

    while True:
        limpiar_pantalla()
        print('\n')
        print('Estructura de Datos I')
        print('Proyecto Final\n')

        opcion_elegida = desplegar_lista(1,6,menu_principal)
                
        # Pilas
        if opcion_elegida == 1:      
            from pila import Pila 
            while True:
                limpiar_pantalla()
                pila = Pila()
                print('\nPilas!\n')
                opcion_elegida = desplegar_lista(1,4,opcion_pilas_colas)
                if opcion_elegida == 1:
                    # Ingresar Dato a la Pila
                    dato = input('\nIngrese el Dato a Guardar en la Pila\n')
                    pila.insertar(dato)
                    pausar()
                if opcion_elegida == 2:
                    # Extraer (Eliminar un dato) de la Pila
                    pila.extraer() 
                    pausar()   
                if opcion_elegida == 3:
                    # Visualizar la Pila
                    pila.visualizar()
                    pausar()
                if opcion_elegida == 4:
                    # Salir
                    # Reiniciando Contador
                    opcion_elegida = 0
                    break
        
        if opcion_elegida == 2:
            from cola import Cola
            while True:

                limpiar_pantalla()               
                # Llamando a la Clase Cola
                cola = Cola()

                print('\nColas!\n')

                opcion_elegida = desplegar_lista(1,4,opcion_pilas_colas)
                if opcion_elegida == 1:
                    # Guardar en la Cola
                    dato = input('\nIngrese el Dato a Guardar en la Cola\n')
                    cola.insertar(dato)
                    pausar()
                if opcion_elegida == 2:
                    # Extraer (Eliminar) un dato de la Cola
                    cola.extraer()    
                    pausar()
                if opcion_elegida == 3:
                    # Vizualizar un dato de la cola
                    cola.visualizar()
                    pausar()
                if opcion_elegida == 4:
                    # Salir
                    # Reiniciando Contador
                    opcion_elegida = 0
                    break
        if opcion_elegida == 3:
            from arbol import Arbol,Nodo

            # Llamando a la Clase Arbol
            arbol = Arbol()

            while True:
                limpiar_pantalla()
                print('\nArboles Binarios!\n')
                opcion_elegida = desplegar_lista(1,5,opcion_arboles)
                if opcion_elegida == 1:
                    
                    # Ingresar datos
                    # Esta es la unica parte del programa en la que no se puede trabajar con valores
                    # alfanumericos, debido al sistema de busqueda por nodo que se implementó

                    print('Solo puedes agregar numeros enteros en esta parte del programa... Cuidado!')
                    dato = askInt("Ingresa un dato\n")
                    nodo = Nodo(dato)
                    arbol.agregar(nodo)
                    pausar()
                if opcion_elegida == 2:
                    # Recorrido PreOrden
                    print('\nRecorrido PreOrden\n')
                    arbol.preorden(arbol.raiz) 
                    pausar()   
                if opcion_elegida == 3:
                    # Recorrido PostOrden
                    print('\nRecorrido PostOrden\n')
                    arbol.postorden(arbol.raiz)
                    pausar()
                if opcion_elegida == 4:
                    # Recorrido EnOrden
                    print('\nRecorrido EnOrden\n')
                    arbol.enorden(arbol.raiz)
                    pausar()
                if opcion_elegida == 5:
                    # Salir
                    opcion_elegida = 0
                    break
                # Reiniciando Contador
        if opcion_elegida == 4:
            from listas import Lista,Nodo
            from funciones import crear_menu
            while True:
                limpiar_pantalla()
                # cargando las listas del archivo txt

                listas = cargar('./listas.txt',[]) 
                print('\nListas Enlazadas!\n')
                opcion_elegida = desplegar_lista(1,5,opcion_lista)
                menu = crear_menu(listas)
                if opcion_elegida == 1:
                    # Creando Lista
                    lista = Lista()
                    lista.crear_lista()
                    print('Lista Creada...')
                    pausar()
                if opcion_elegida == 2:
                    # Agregar elementos a la Lista
                    # Verificando si hay listas presentes
                    if not len(listas):
                        print('\nNo hay Listas! Crea Una Primero\n')
                        pausar()
                    else:


                        # Preguntando al Usuario que lista desea modificar
                        print('\nEscoge la lista que deseas modificar\n')
                        opcion_elegida = desplegar_lista(1,len(listas),menu)
                        opcion_elegida = opcion_elegida-1
                        
                        # Eligiendo la lista seleccionada por el usuario y 
                        # recolectando los datos de la lista seleccionada
                        lista = listas[opcion_elegida]
                        datos = []
                        for dato in lista.values():
                            datos.append(dato)

                        # Inicializando el ultimo dato y el nodo anterior
                        # para evitar errores de codigo
                        ultimo_dato = False
                        nodo_anterior = False

                        # Verificando si hay datos
                        if len(datos):
                            ultimo_dato = datos[-1]
                            nodo_anterior = Nodo(ultimo_dato['valor'],opcion_elegida)
                            nodo_anterior.proximo = ultimo_dato['proximo']
                            
                        # Pidiendo el dato a agregar

                        dato = input('\nIngresa el nuevo dato\n')
                        nodo = Nodo(dato,opcion_elegida)

                        # Verificando si existe el nodo_anterior para insertarlo con el 
                        # apuntador hacia el siguiente...
                        if nodo_anterior != False:
                            nodo.insertar_elemento(nodo_anterior)
                            nodo_anterior = nodo
                        else:
                            nodo.insertar_elemento(None)

                    print('Elemento Añadido a la Lista')
                    pausar()

                if opcion_elegida == 3:
                    
                    
                    # Desplegando lista al usuario
                    print('\nEscoge la lista que deseas modificar\n')
                    opcion_elegida = desplegar_lista(1,len(listas),menu)
                    opcion_elegida = opcion_elegida-1
                    lista = Lista(opcion_elegida)
                    if len(listas[opcion_elegida].keys()) == 0:
                        print('La lista esta vacia, no se puede eliminar')
                        pausar()
                    else:
                        # Desplegando datos y preguntando al usuario cual eliminar
                        print('\nElige el elemento que deseas eliminar\n')
                        datos = []
                        for dato in listas[opcion_elegida].values():
                            datos.append(dato['valor'])
                        opcion_elegida = desplegar_lista(1,len(datos),datos)
                        dato = datos[opcion_elegida-1]

                        # Eliminando el dato
                        lista.eliminar(dato)
                        print('Dato Eliminado')
                        pausar()

                if opcion_elegida == 4:
                    # Recorrer lista

                    # Haciendo que el usuario escoja la lista a recorrer
                    print('\nEscoge la lista que deseas recorrer\n')
                    opcion_elegida = desplegar_lista(1,len(listas),menu)
                    opcion_elegida = opcion_elegida-1

                    # Seleccionando lista escogida por el cliente
                    lista = Lista(opcion_elegida)
                    lista.reccorrer_lista()
                    pausar()
                if opcion_elegida == 5:
                    # Salir
                    opcion_elegida = 0
                    break
                # Reiniciando el contador de opcion
        if opcion_elegida == 5:
            # Grafos
            print('\nGrafos!\n')
            from grafo import mostrar_grafo
            # Mostrando grafos
            mostrar_grafo()
            pausar()
            opcion_elegida = 0
        if opcion_elegida == 6:
            # Salir del Programa
            break
    # Saludo Final
    print('\nMuchas Gracias por consultar este programa, que tenga un buen dia!')