'''Creare la clase "reproduccion" la cual sera
similar a una lista simple doble'''
import nodoCancion
NC=nodoCancion
class reproduccion(object): #holi
    def __init__(self): # creo las etiquetas para orientar la lista
        self.__primero=None
        self.__ultimo=None
        self.__cont=0
    def getVacio(self):# verificador de que si la lista esta vacia
        if self.__primero==None:
            return True
    def getNodoPrimero(self):
        if self.getVacio()==True:
            print("Reproductor de musica vacio")
            return
        else:
            return self.__primero
    def getNodoUltimo(self):
        if self.getVacio()==None:
            print("Reproductor de musica vacio")
            return
        else:
            return self.__ultimo
    def setCancionUltima(self,n,i,d):
        aux=NC.cancion(n,i,d)
        if self.getVacio()==True:
            self.__primero=self.__ultimo=aux
            print("Cancion agregada a la lista de reproduccion")
            cont+=1
            return
        elif self.__primero==self.__ultimo:
            self.__primero.sgte=aux
            self.__ultimo=aux
            self.__ultimo.ant=self.__primero
            print("cancion agregada a la lista de reproduccion")
            self.__cont+=1
            return
        else:
            temp=self.__primero
            validar=True
            while(validar):
                if temp==self.__ultimo:
                    self.__ultimo.sgte=aux
                    aux.ant=self.__ultimo
                    self.__ultimo=aux
                    self.__ultimo.sgte=self.__primero
                    print("Cancion agregada a la lista de reproduccion")
                    self.__cont+=1
                    validar=False
                    return
                else:
                    temp=temp.sgte
    def imprimirLista(self):
        if self.getVacio()==True:
            print("No hay cancion en la lista de reproduccion")
            return
        else:
            temp=self.__ultimo
            print("Nombre de la cancion:",temp.getNombre())
            print("Interprete:",temp.getInterprete())
            print("Duracion de la cancion:"temp.getDuracion())
            
            
        
        
        
            
