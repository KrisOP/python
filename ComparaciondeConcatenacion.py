"""edad=7

if 0<edad<100:#concatenacion de operador de comparadores
    print ("Edad es correcta")
else:
    print ("Edad incorrecta")"""

salario_presidente=int(input("Introduce el salario del presidente: "))

print("Salario Presidente: " + str(salario_presidente))   

salario_director=int(input("Introduce el salario_director: "))

print("salario_director: " + str(salario_director))   

salario_jefe_area=int(input("Introduce el salario_jefe_area: "))

print("salario_jefe_area: " + str(salario_jefe_area))   

administrativo=int(input("Introduce el administrativo: "))

print("administrativo: " + str(administrativo))   

if administrativo<salario_jefe_area<salario_director<salario_presidente:
     print ("todo funciona excelente")
else:
    print ("Algo falla en la empresa")