from funciones import guardar_clientes,cargar_clientes


clientes = cargar_clientes()

# Para este punto, el clientes es un arreglo (como se puede ver en "funciones.py") 
# y esta cargado con todos los clientes que se encuentran en el archivo "clientes.txt"



class Cliente():
    '''
        Esta es una clase(objeto) que sirve para manejar mas facilmente en 
        "cajero.py" las funcionalidades del cliente en cuestion, a saber:

        1. Depositar
        2. Retirar
        3. Añadir Cliente (SOLO EN DESARROLLO)
    '''
    def __init__(self,nombre,saldo,clave):
        self.nombre = nombre
        self.saldo = saldo
        self.clave = clave
    
    def depositar(self,deposito):
        '''
            Funcion que se encarga de realizar el deposito a la cuenta del cliente,
            guardarlo en el arreglo y luego guardarlo en el archivo "clientes.txt"
            mediante la funcion "guardar_clientes(clientes)" que se encuentra en 
            "funciones.py"
        '''
        print('\n')
        for cliente in clientes:
    
            if cliente['nombre'] == self.nombre:
                self.saldo = float(cliente['saldo']) + deposito
                cliente['saldo'] = self.saldo
                
                print('Deposito Realizado!!\n')
                print('Nuevos Datos')
                print('\nCliente:',self.nombre)
                print('Saldo: B/.',float(self.saldo))
                
                guardar_clientes(clientes)
                return True

    def retirar(self,retiro):
        '''
            Funcion que se encarga de realizar el retiro a la cuenta del cliente,
            guardar el saldo en el arreglo y luego guardar todo en el archivo "clientes.txt"
            mediante la funcion "guardar_clientes(clientes)" que se encuentra en 
            "funciones.py"
        '''
        
        print('\n')
        for cliente in clientes:
            if cliente['nombre'] == self.nombre:
                self.saldo = float(cliente['saldo']) - retiro
                cliente['saldo'] = self.saldo
                
                print('Retiro Realizado!!\n')
                print('Nuevos Datos')
                print('\nCliente:',self.nombre)
                print('Saldo: B/.',float(self.saldo))
                
                guardar_clientes(clientes)
                return True

    def anadir_usuario(self):
        '''
            Funcion solo hecha con fines de desarrollo para poder tener usuarios de prueba

            Funcion para añadir un nuevo usuario a "clientes.txt".
        '''
        with open('./clientes.txt','a') as _clientes:
            cliente = {'nombre':self.nombre,'saldo':self.saldo}
            
            _clientes.write('XXXXXXXXXXXXXXXXX\n')
            _clientes.write(repr(cliente))
            _clientes.write('\n')
            _clientes.write('XXXXXXXXXXXXXXXXX\n')
        
        return True