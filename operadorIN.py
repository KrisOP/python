print("ASIGNATURAS OPTATIVAS DEL ANIO 2018")

print ("Informatica Grafica - Pruebas de Software - Usabilidad y Accesibilidad")
opcion=input("Escriba la asignatura escogida:  ")

asignatura=opcion.lower()#convertir string a minuscula
print(asignatura)

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print ("asignatura elegida "+asignatura)
else:
    print ("La asignatura escogida no existe")