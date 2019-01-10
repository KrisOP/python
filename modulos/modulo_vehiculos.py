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


class Furgoneta (Vehiculos):
    def carga (self,cargar):
        self.cargado=cargar
        if (self.cargado):
            return "la furgoneta esta cargada"
        else:
            return "la furgoneta no esta cargada"



class Moto (Vehiculos):#la clase moto hereda de la clase vehiculos
    ##ESTA CLASE TIENE 5 METODOS, 4 HEREDADOS Y UNO DEFINIDO DENTRO
    hcaballito=""
    def caballito (self):
        self.hcaballito="haciendo el caballito"
    def estado(self):
        print ("marca: ", self.marca, "\nModelo:", self.modelo,"\nEn marcha: ",self.enmarcha, "\nAcelerando: ",self.acelera, "\nFrenando:",self.frena, "\nActividad especial:", self.hcaballito)


class VElectricos(Vehiculos):
    def __init__(self,marca,modelo):
       self.autonomia=100
       super().__init__(marca,modelo)#llamando a metodo init de la clase padre

    def cargarEnergia(self):
         self.cargando=True




