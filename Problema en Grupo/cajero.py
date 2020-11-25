from ask import askString,askInt
from clases import Cliente,clientes
from funciones import buscar_cliente

# Problema Grupo B
# Se desea simular el comportamiento de un Cajero Automático para 
# ello se va a tener un menú como el que sigue
# MENU PINCIPAL
# 1. CONSULTA
# 2. DEPOSITO
# 3. RETIRO
# 4. SALIDA


opciones = ['Consulta','Depósito','Retiro','Salida']


if __name__ == "__main__":
    while True:
        print('\nMenu Principal \n')
        
        # Imprimiendo opciones en pantalla
        i=1
        for opcion in opciones:
            print(f'{i}.) {opcion}')
            i+=1

        print('\n')
        opcion_elegida = askInt('OPCION')
        opcion_elegida = int(opcion_elegida)

# Opción 1
# Si el usuario presiona 1 el programa debe 
# verificar si el cliente existe dentro del arreglo 
# y luego entonces mostrar el saldo del cliente

        if opcion_elegida == 1:
            print('\n')
            
            nombre = askString("Ingrese el nombre del cliente")
            cliente = buscar_cliente(nombre)
            
            if cliente:
                clave = askInt('\nIngrese clave')
                
                if clave == cliente.clave:
                    print('\nDatos del Cliente')
                    print('\nCliente:',cliente.nombre)
                    print('Saldo: B/.',float(cliente.saldo))
                    print('\nConsulta Finalizada!')
                else:
                    print('\nError!! Clave Incorrecta\n')

            
# Opción 2
# Si el usuario presiona el 2 significa que desea depositar, para ello primero se 
# verifica si existe dentro del arreglo y luego se solicita la cantidad que desea 
# depositar. Una vez registrada la cantidad a depositar el programa deberá imprimir 
# el saldo actual. Recuerde enviar mensajes de error si el usuario no existe dentro 
# de nuestro arreglo.
        
        if opcion_elegida == 2:
            print('\n')
            
            nombre = askString("Ingrese el nombre del cliente")
            cliente = buscar_cliente(nombre)
            
            if cliente:
                clave = askInt('\nIngrese clave')
                
                if clave == cliente.clave:
                    deposito = askInt('\nIngrese la cantidad a depositar')
                    deposito = float(deposito)
                    cliente.depositar(deposito)
                    print('\nTransacción Finalizada!')
                else:
                    print('\nError!! Clave Incorrecta\n')

# Opción 3
# Si el usuario presiona la opción 3 significa que desea hacer un retiro 
# lo primero que el programa debe realizar es la búsqueda de ese cliente 
# dentro del arreglo para ver si existe, una vez verificado debe mostrar 
# el saldo actual y nombre del cliente y luego solicitar el monto a retirar. 
# Aquí hay que validar que el monto a retirar sea menor de lo que tiene en 
# el saldo actual, si excede esa cantidad el programa deberá enviar un mensaje de error.

        if opcion_elegida == 3:
            print('\n')
            
            nombre = askString("Ingrese el nombre del cliente")
            cliente = buscar_cliente(nombre)
            
            if cliente:
                clave = askInt('\nIngrese clave')
                
                if clave == cliente.clave:
                    print('\nCliente:',cliente.nombre)
                    print('Saldo: B/.',float(cliente.saldo))

                    retiro = askInt('Ingrese el monto a Retirar')
                    retiro = float(retiro)
                    
                    if retiro<cliente.saldo:
                        cliente = cliente.retirar(retiro)
                        print('\nTransacción Finalizada!')
                    else:
                        print('\nError! El monto a retirar se excede del saldo disponible')
                        
                else:
                    print('\nError!! Clave Incorrecta\n')


#  Opción 4
# En ésta opción el usuario está decidiendo salir del programa.

        if opcion_elegida == 4:
            print('\nMuchas gracias por su transaccion o consulta')
            print('Nos Vemos Pronto!')
            break

# Opcion 5 (Solo para desarrollo)
# Esta es una opcion que yo cree, puesto que no tenia usuarios para probar.
# La opcion solamente crea un nuevo usuario con clave, saldo inicial y nombre.
        if opcion_elegida == 5:
            nombre = input("Ingrese el nombre\n")
            
            saldo = askInt('Ingrese el Saldo Inicial')
            saldo = int(saldo)
            
            clave = askInt('\nIngrese Clave')
            clave = int(clave)
            
            cliente = Cliente(nombre,saldo,clave)
            cliente.anadir_usuario()

# Para el desarrollo de este programa, deberá hacer uso de Funciones y arreglos. 
# Sugerencia puede tener un arreglo de estructura que tenga un campo que 
# indique la clave del usuario, otro campo que indique el nombre y otro 
# campo que indique el saldo actual.

