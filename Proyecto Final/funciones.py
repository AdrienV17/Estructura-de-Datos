from ask import askInt

def desplegar_lista(inicio,final,menu):
    '''
    Funcion que se encarga de desplegar la lista de opciones y
    verificar su rango de respuestas, comprobando que el usuario 
    haya ingresado un valor (numerico), situado entre los 
    parametros dados. De no ser el caso, la funcion crea un bucle
    desplegando el menu anterior, hasta que el usuario responda 
    correctamente, luego, se retorna el valor de respuesta en un 
    dato tipo entero.
    '''
    opcion_elegida = ''
    while True:
        # Desplegando el menu 
        # Inicializando un valor centinela ("i") para enumerar cada 
        # opcion através de un bucle
        i = 1
        for opcion in menu:
            print(f'{i}.) {opcion}')
            i+=1

        opcion_elegida = askInt('\nEscoge un Numero')
        opcion_elegida = int(opcion_elegida)

        __final = final + 1
        if opcion_elegida not in range(inicio,__final):
            print(f'Debes escoger un numero entre {inicio} y {final}')
        else:
            break
    
    return opcion_elegida

def cargar(archivo,sino):
    '''
    Funcion que extrae toda la informacion de un archivo,
    la evalua como codigo y la retorna. Contiene un atributo "sino",
    por si el archivo no contiene valores
    '''
    try:
        with open(archivo) as info:
            info = eval(info.read())
            return info
    except:
        return sino

def guardar(archivo,datos):
    '''
    Funcion que guarda toda la informacion dada en un archivo txt
    '''
    with open(archivo,'w') as info:
        info.write(repr(datos))

def crear_menu(listas):
    '''
    Funcion que crea el menu para las opciones de las listas enlazadas
    '''
    menu = []
    # Creando un menu a partir de las listas existentes...
    for lista in listas:
        opcion = False
        for valor,proximo in lista.items():
            if opcion !=False: 
                opcion = opcion + ', ' + valor
            else:
                opcion = valor
        if opcion == False:
            opcion = 'Lista Sin Elementos'
        menu.append(opcion) 
    return menu

from os import system

def limpiar_pantalla():
    '''
    Funcion que limplia la pantalla de la consola
    '''
    system('cls')

def pausar():
    '''
    Funcion que pausa la Consola para evitar que la informacion se vaya...
    '''
    print('\n')
    system('pause')
    print('\n')
