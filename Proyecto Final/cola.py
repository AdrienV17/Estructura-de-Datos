class Cola:
    '''
    Clase que emula la funcion de una cola en Python.
    Guarda los datos almacenados por el usuario en un archivo txt
    '''
    def __init__(self):
       self.cola = []

    def guardar_cola(self):
        '''
        Método que guarda la cola en un archivo txt
        '''
        with open('./cola.txt','w') as cola:
            cola.write(repr(self.cola))

    def cargar_cola(self):
        '''
        Metodo que extrae la cola guardada en el archivo txt y la convierte a formato 
        de programacion
        '''
        with open('./cola.txt') as cola:
           self.cola = eval(cola.read())

    def insertar(self,dato):
        '''
        Metodo que se encarga de insertar el dato dado por el usuario a la cola
        y retorna el ultimo valor agregado.
        '''
        self.cargar_cola()
        self.cola.append(dato)
        print('Dato Insertado a la cola!')
        print(f'Ultimo Elemento: {self.cola[-1]}')
        self.guardar_cola()
        return self.cola[-1]

    def extraer(self):
        '''
        Metodo que se encarga de remover el primer valor de la cola,
        no necesita parametros puesto que, en el funcionamiento de la cola,
        la operacion de extraccion solo remueve el primer valor agregado.
        '''
        self.cargar_cola()
        if len(self.cola):
            dato_eliminado = self.cola.pop(0)
            self.guardar_cola()
            if len(self.cola):
                print('Dato Eliminado de la cola')
                if len(self.cola) == 0:
                    print('La cola ha querado Vacia!')
                return dato_eliminado
            else:
                print('La cola está vacia, procura insertar algun dato en ella.')
        else:
            print('La cola está vacia, procura insertar algun dato en ella.')
    def visualizar(self):
        '''
        Metodo que se encarga de visualizar la cola mostrando los ultimos elementos agregados
        como primeros, de acuerdo al orden de visualizacion de la cola
        '''
        self.cargar_cola()
        print('\nDatos de la cola\n')
        i = 1
        for dato in self.cola:
            print(f'{i}.) {self.cola[i*-1]}')
            i+=1
        print(f'\nCantidad de Datos:{len(self.cola)}')