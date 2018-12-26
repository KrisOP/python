distancia= int (input("ingrese la distacia de su domicilio en km"))
print (distancia)
hermanos=int(input("Ingrese la cantidad de numeros de hermanos en el centro"))
print (hermanos)
salario_anual=int(input("Introduce el salario Anual"))
print(salario_anual)

if distancia>40 and hermanos>2 and salario_anual<=2000:
    print("Se le puede otorgar beca")
else:
    print("No se le puede otorgar ninguna beca")
    