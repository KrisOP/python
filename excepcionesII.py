def divide():
    try:
        op1=(float(input("introduce el primer numero")))
        op2=(float(input("introduce el segundo numero")))

        print ("La division es: " + str(op1/op2))
    except ValueError:
        print ("El valor introducido es erroneo")
    except ZeroDivisionError:
        print ("No se puede dividir entre 0")
    finally:#todo lo que esta dentro de finally siempre se va a ejecutar, tanto haya o no error
        
        print("calculo finalizadoo")

divide()