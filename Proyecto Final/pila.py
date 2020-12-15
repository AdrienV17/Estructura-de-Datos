class Pila:
    '''
    Clase que emula la funcion de una pila en Python.
    Guarda los datos almacenados por el usuario en un archivo txt
    '''
    def __init__(self):
        self.pila = []
    def guardar_pila(self):
        '''
        Método que guarda la pila en un archivo txt
        '''
        with open('./pila.txt','w') as pila:
            pila.write(repr(self.pila))
    def cargar_pila(self):
        '''
        Metodo que extrae la pila guardada en el archivo txt y la convierte a formato 
        de programacion
        '''
        with open('./pila.txt') as pila:
            self.pila = eval(pila.read())
    def insertar(self,dato):
        '''
        Metodo que se encarga de insertar el dato dado por el usuario a la pila
        y retorna el ultimo valor agregado.
        '''
        self.cargar_pila()
        self.pila.append(dato)
        print('Dato Insertado a la Pila!')
        print(f'Ultimo Elemento: {self.pila[-1]}')
        self.guardar_pila()
        return self.pila[-1]
    def extraer(self):
        '''
        Metodo que se encarga de remover el ultimo valor de la pila,
        no necesita parametros puesto que, en el funcionamiento de la pila,
        la operacion de extraccion solo remueve el ultimo valor agregado.
        '''
        self.cargar_pila()
        if len(self.pila):
            dato_eliminado = self.pila.pop()
            print('Dato Eliminado de la Pila')
            self.guardar_pila()
            if len(self.pila):
                print(f'Ultimo Elemento Actual: {self.pila[-1]}')
                return dato_eliminado
            else:
                print('\nLa Pila ha quedado vacia, procura insertar algun dato en ella.')
        else:
            print('\nLa Pila está vacia, procura insertar algun dato en ella.')
    def visualizar(self):
        '''
        Metodo que se encarga de visualizar la pila mostrando los ultimos elementos agregados
        como primeros, de acuerdo al orden de visualizacion de la pila
        '''
        self.cargar_pila()
        print('\nDatos de la Pila\n')
        if (len(self.pila)):
            i = 1
            for dato in self.pila:
                print(f'{i}.) {self.pila[i*-1]}')
                i+=1
            print(f'\nCantidad de Datos:{len(self.pila)}')
        else:
            print('\nLa Pila está vacia, procura insertar algun dato en ella.')
