import pickle



class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True

    def estado(self):
        print ("marca: ", self.marca, "\nModelo:", self.modelo,"\nEn marcha: ",self.enmarcha, "\nAcelerando: ",self.acelera, "\nFrenando:",self.frena)


coche1=Vehiculos("Mazda", "MX5")
coche2=Vehiculos("Seat", "Leon")
coche3=Vehiculos("Mercedes", "Berlina")


coches=[coche1,coche2,coche3]

fichero=open("losCoches","wb")#crear un fichero externo con permisos de escritura en binario

pickle.dump(coches,fichero)

fichero.close()#cerrar fichero de memoria

del (fichero)#borrar fihero de memoria, NO DE DISCO DURO

ficheroApertura=open("losCoches","rb")#lectura de bytes

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()



for c in misCoches:
    print(c.estado())