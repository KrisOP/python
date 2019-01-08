class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    
    #declaracion de metodo no de funcion. (Las funciones no pertenecen a clases, los metodos si)
    def arrancar(self): #el self viene siendo igual al this en otros lenguajes##recibe como parametro al propio objeto#es decir miCoche.enmarcha=True
       self.enmarcha=True 
    def estado(self):
        if(self.enmarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta detenido"


miCoche=Coche()#instanciando clase

print ("El largo del coche es: ", miCoche.largoChasis)
print ("El coche tiene: ",miCoche.ruedas, "ruedas")
miCoche.arrancar()##llamada al metodo

print (miCoche.estado())


print("***************a continuacion creamos el segundo objeto*********************")

miCoche2=Coche()
print ("El largo del coche es: ", miCoche.largoChasis)
print ("El coche tiene: ",miCoche.ruedas, "ruedas")

print (miCoche2.estado())