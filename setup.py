#configurar paquetes distribuibles


from setuptools import setup

setup(

    name="paqueteCalculos",#crear un paquete distribuible con funciones de potencia y redondeo de paquete calculos
    version="1.0",
    descripcion="Paquete de redondeo y potencia",
    author="Kristopher Ortega",
    author_email="krisortega15@hotmail.es",
    url="kris.com"
    packages=["Calculos","Calculos.redondeo_potencia"]#indicar la ruta donde se encuentra el paquete Calculos

    )