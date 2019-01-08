class Coche():

    def __init__(self):#constructor de la clase (estado inicial de la clase)
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4 #encapsulando la variable rueda//NO PUEDE SER ACCESIBLE DESDE FUERA DE LA CLASE(MODIFICAR)
        self.__enmarcha=False
    
    #declaracion de metodo no de funcion. (Las funciones no pertenecen a clases, los metodos si)
    def arrancar(self,arrancamos): #el self viene siendo igual al this en otros lenguajes##recibe como parametro al propio objeto#es decir miCoche.enmarcha=True
       self.__enmarcha=arrancamos

       if (self.__enmarcha):
           chequeo=self.__chequeo_interno()

       if(self.__enmarcha and chequeo):
          return "el coche esta en marcha"
       elif (self.__enmarcha and chequeo==False):
           return "algo ha ido mal en el chequeo, no podemos arrancar"
       else:
            return "el coche esta detenido"

    def estado(self):

        print ("el coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, "y un largo de ", self.__largoChasis)

    def __chequeo_interno(self):##encapsulando metodos//solo se puede acceder al metodo dentro de la clase
        print ("realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

miCoche=Coche()#instanciando clase

#print ("El largo del coche es: ", miCoche.largoChasis)
#print ("El coche tiene: ",miCoche.__ruedas, "ruedas")
print(miCoche.arrancar(True))##llamada al metodo

miCoche.estado()


print("***************a continuacion creamos el segundo objeto*********************")

miCoche2=Coche()
#print ("El largo del coche es: ", miCoche.largoChasis)
#print ("El coche tiene: ",miCoche.ruedas, "ruedas")#SI ESTA ENCAPSULADO EL ATRIBUTO NO PODEMOS LLAMARLO DESDE FUERA DE LA CLASE
print(miCoche2.arrancar(False))
#miCoche2.ruedas=2#NO SE MODIFICA PORQUE ESTA FUERA DE LA CLASE
miCoche2.estado()
