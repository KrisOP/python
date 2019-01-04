def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:#captura o control de excepcion, para que las siguientes lineas de codigos se ejecuten
	    return num1/num2
    #ZeroDivisionError ES EL NOMBRE DEL ERROR QUE NOS MUESTRA AL EJECUTAR EL PROGRAMA CUANDO QUEREMOS DIVIDIR ENTRE 0
    except ZeroDivisionError:#en caso que no se consiga realizar la division (NO SE PUEDE DIVIDIR ENTRE 0)
        print("No se puede dividir entre 0")
        return "operacion erronea"
	

op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecúción del programa ")
