import pickle

class Persona:
    def __init__(self, nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print ("se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self):#convertir en cadena de texto la informacion de un objeto, para verlos en un archivo externo
        return "{} {} {} ".format(self.nombre,self.genero,self.edad)

class ListaPersonas:
    personas=[]

    def __init__ (self):
        listaDePersonas=open("ficheroExterno","ab+")#agregar informacion binaria
        listaDePersonas.seek(0)

        try:

            self.personas=pickle.load(listaDePersonas)
            print ("se cargaron {} personas del fichero externo". format(len(self.personas)))
        except :
            print ("el fichero esta vacio")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)


    def agregarPersonas(self,p):
        self.personas.append(p)#agregar la persona p  a la lista
        self.guardarPersonasEnFicheroExterno()
    
    def mosstrarPersonas(self):
        for p in self.personas:
            print (p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print ("La informacion del fichero externo es la siguiente")
        for p in self.personas:
            print(p)

miLista=ListaPersonas()
p=Persona("Angela","femenino",34)
miLista.agregarPersonas(p)
miLista.mostrarInfoFicheroExterno()
"""p=Persona("kris","hombre",22)
miLista.agregarPersonas(p)
p=Persona("Karla","femenina",21)
miLista.agregarPersonas(p)

miLista.mosstrarPersonas()"""

