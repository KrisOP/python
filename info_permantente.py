import pickle

class Persona:
    def __init__(self, nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print ("se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self):#convertir en cadena de texto la informacion de un objeto, para verlos en un archivo externo
        return "{} {} {} ".format(self.nombre,self.genero,self.edad)


p=Persona("kris","hombre","22")