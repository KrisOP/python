class Persona():
    
    def __init__(self,nombre,edad,lugar_residencia):

        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion (self):
        print ("nombre: ", self.nombre, "Edad: ",self.edad, "Residencia: ",self.lugar_residencia)

class empleado(Persona):#hereda de la clase persona
    def __init__(self, salario, antiguedad):

        self.salario=salario
        self.antiguedad=antiguedad
    
    Antonio=Persona("Antonio", 55, "Nicaragua")

    Antonio.descripcion()