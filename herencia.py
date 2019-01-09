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

class Moto (Vehiculos):#la clase moto hereda de la clase vehiculos
    ##ESTA CLASE TIENE 5 METODOS, 4 HEREDADOS Y UNO DEFINIDO DENTRO
    hcaballito=""
    def caballito (self):
        hcaballito="voy a hacer el caballito"




miMoto=Moto("Honda", "CRB")
miMoto.estado()
