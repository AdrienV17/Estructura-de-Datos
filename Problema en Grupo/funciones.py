def guardar_clientes(clientes):
    '''
        Funcion para guardar un cliente en "clientes.txt".

    '''
    with open('./clientes.txt','w') as clientes_db:
       for cliente in clientes:
            cliente = {'nombre':cliente['nombre'],'saldo':cliente['saldo'],'clave':cliente['clave']}
            
            clientes_db.write('XXXXXXXXXXXXXXXXX\n')
            clientes_db.write(repr(cliente))
            clientes_db.write('\n')
            clientes_db.write('XXXXXXXXXXXXXXXXX\n')
    
    return True
def cargar_clientes():
    '''
        Funcion que guarda todos los datos de "clientes.txt" y los retorna en un 
        arreglo. 
    '''
    clientes = []
    
    with open('./clientes.txt') as _clientes:
        lineas = _clientes.readlines()
        for linea in lineas:
            
            if 'nombre' in linea:
                clientes.append(eval(linea))
    
    return clientes        

def buscar_cliente(nombre):
    '''
        Funcion que busca a un cliente dando el nombre como parámetro, y retorna
        un objeto Cliente (encontrado en "clases.py") con los datos del cliente encontrado.
    '''
    from cajero import clientes
    from clases import Cliente
    
    if len(clientes):
        
        for cliente in clientes:
            
            if cliente['nombre'] == nombre:
                print('\nCliente encontrado!!')
                
                cliente = Cliente(cliente['nombre'],cliente['saldo'],cliente['clave'])
                return cliente
        
        print(f'\nEl Usuario de nombre {nombre} no existe')
    else:
        print('\nNo se encuentran clientes en la base de datos')
