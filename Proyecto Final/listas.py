from funciones import cargar,guardar

class Nodo:
    def __init__(self,valor,lista):
        self.lista = lista
        self.valor = valor
        self.proximo = None

    def insertar_elemento(self,nodo_anterior):  
        lista = Lista(self.lista)
        if nodo_anterior:    
            nodo_anterior.proximo = self.valor
            lista.insertar(nodo_anterior)
        lista.insertar(self)


class Lista:
    '''
    Clase que emula la funcion de una lista en Python.
    Guarda los datos almacenados por el usuario en un archivo txt
    '''
    def __init__(self,numero=None):
        self.listas = []
        self.numero = numero
        self.proximo = None

    def crear_lista(self):
        self.listas = cargar('./listas.txt',[])
        self.listas.append({})
        guardar('./listas.txt',self.listas)
        
    def insertar(self,nodo):

        self.listas = cargar('listas.txt',[])
        lista = self.listas[self.numero]
        lista[nodo.valor] = {'valor':nodo.valor,'proximo':nodo.proximo}
        guardar('./listas.txt',self.listas)
        
    def eliminar(self,dato):
        self.listas = cargar('listas.txt',[])
        lista = self.listas[self.numero]
        nueva_lista = {}
        for nodo,valores in lista.items():
            if nodo != dato:
                nueva_lista[nodo] = valores
        self.listas[self.numero] = nueva_lista
        guardar('./listas.txt',self.listas)
    def reccorrer_lista(self):
        self.listas = cargar('listas.txt',[])
        lista = self.listas[self.numero]
        if len(lista):
            for dato in lista.values():
                print('\n')
                valor = dato['valor']
                
                print(f'Nodo: {valor}')
                print(f'xxxxxxxxxxxxxxxxxxxxx\n')
        else:
            print('La Lista esta vacía, ingrese primero un elemento a ella')






















    # def guardar_lista(self):
    #     '''
    #     Método que guarda la lista en un archivo txt
    #     '''
    #     with open('./lista.txt','w') as lista:
    #         lista.write(repr(self.lista))

    # def cargar_lista(self):
    #     '''
    #     Metodo que extrae la lista guardada en el archivo txt y la convierte a formato 
    #     de programacion
    #     '''
    #     with open('./lista.txt') as lista:
    #        self.lista = eval(lista.read())

    # def insertar(self,nodo):
    #     lista = self.cargar_lista()
    #     if lista == '':
    #         lista = {}
    #    
