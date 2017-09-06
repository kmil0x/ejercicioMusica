'''Creare la clase "cancion" con la cual se ingresara las canciones
para crear listas de reproduccion'''
class cancion(object):# este sera el nodo
    def __init__(self,nombre,interprete,duracion):#construtor que agrega los temas
        self.__nombre=nombre
        self.__interprete=interprete
        self.__duracion=duracion
        self.__sgte=None
        self.__ant=None
    def getNombre(self):
        return self.__nombre
    def getInterprete(self):
        return self.__interprete
    def getDuracion(self):
        return self.__duracion
    
