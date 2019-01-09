class Persona():
    
    def __init__(self,nombre,edad,lugar_residencia):

        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion (self):
        print ("nombre: ", self.nombre, "Edad: ",self.edad, "Residencia: ",self.lugar_residencia)

class empleado(Persona):#hereda de la clase persona
    def __init__(self, salario, antiguedad,nombre_empleado, edad_empleado,residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)##llama al metodo init de la clase padre

        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion (self):
        super().descripcion()
        print ("\n El salario: ",self.salario, "\nLa antiguedad",self.antiguedad)
        # print ("nombre: ", self.nombre, "Edad: ",self.edad, "Residencia: ",self.lugar_residencia)
    
Kris=empleado(1500,15,"Kris",22, "Nicaragua")

Kris.descripcion()

print (isinstance(Kris,Persona))#Manuel es de la clase empleado