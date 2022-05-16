from sys import prefix

class casilla:
    def __init__(self,nombre):
        self.nombre=nombre
        self.vecinos=[]
        self.visitado=False
        
    def add_vecino(self,casilla):
        self.vecinos.append(casilla)
    def get_vecinos(self):
        return self.vecinos
    def ver(self):
        print (self.nombre)
        for i in self.vecinos:
            i.ver()
        print (self.vecinos)
    def add_vecino(self,casilla):
        self.vecinos.append(casilla)
    def Setvisitado(self):
        self.visitado=True
    def getvisitado(self):
        return self.visitado

        
    
class arbol:
        def __init__(self,posicion) :
            self.posicion=posicion
            self.hijo=[] #pueden ser 00, 1 o más hijos
            self.padre=None #el nodo inicial no puede tener paadre
        def agrega_hijo(self, Nuevo_hijo):
            # hay que asignarle el padre a este nuevo hijo, ya que con
            #self.hijo.append le da un hijo al padre pero no le dice 
            #al hijo quien es el padre
            Nuevo_hijo.padre=self
            self.hijo.append(Nuevo_hijo)
        def profundidad(self):
            altura=0
            pad=self.padre
            while pad:
                altura+=1
                pad=pad.padre
            return altura
            
        def imprime(self):
            espacio=' '* self.profundidad()*3
            masespacio = espacio+"---" if self.padre else ""
            print(masespacio+ self.posicion)
            if self.hijo:
                for hijo in self.hijo:
                    hijo.imprime()
        def creararbol():
            Raiz=arbol("2,3")
            hijo=arbol("1,3")
            hijo.agrega_hijo(arbol("0,3"))
            hijo.agrega_hijo(arbol("0,4"))
            otrohijo=arbol("2,4")
            otrohijo.agrega_hijo(arbol("2,5"))
            otrootro=arbol("5,5")
            otrohijo.agrega_hijo(otrootro)
            Raiz.agrega_hijo(hijo)
            Raiz.agrega_hijo(otrohijo)
            return Raiz
                    
        