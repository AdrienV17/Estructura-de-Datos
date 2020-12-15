class Nodo():
    def __init__(self,dato=None):
        self.izq = None
        self.der = None
        self.dato = dato
    def __str__(self):
        return "%s" %(self.dato)
class Arbol():
    def __init__(self,raiz=None):
        self.raiz = raiz
    def agregar(self,elemento):
        '''
        Método que Agrega un nodo al arbol binario
        '''
        if self.raiz == None:
            self.raiz = elemento
            print('Nodo Agregado al Arbol')
        else:
            aux = self.raiz
            padre = None
            while aux != None:
                padre = aux
                if int(elemento.dato) >= int(aux.dato):
                    aux = aux.der 
                else:
                    aux = aux.izq
            if int(elemento.dato) >= int(padre.dato):
                padre.der = elemento
            else:
                padre.izq = elemento
            print('Nodo Agregado al Arbol')
    def preorden(self,elemento):
        '''
        Metodo que recorre el arbol binario en Pre Orden
        '''
        if elemento != None:
            print(elemento)
            self.preorden(elemento.izq)
            self.preorden(elemento.der)
    def postorden(self,elemento):
        '''
        Metodo que recorre el arbol binario en Post Orden
        '''
        if elemento != None:
            self.postorden(elemento.izq)
            self.postorden(elemento.der)
            print(elemento)
    def enorden(self,elemento):
        '''
        Metodo que recorre el arbol binario en En Orden
        '''
        if elemento != None:
            self.enorden(elemento.izq)
            print(elemento)
            self.enorden(elemento.der)
    def raiz(self):
        '''
        Metodo que retorna la raiz del arbol binarios
        '''
        return self.raiz
