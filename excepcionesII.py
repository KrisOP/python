def divide():
    try:
        op1=(float(input("introduce el primer numero")))
        op2=(float(input("introduce el segundo numero")))

        print ("La division es: " + str(op1/op2))
    #except ValueError:
    except:
        print ("ha ocurrido un error")
        """print ("El valor introducido es erroneo")
    except ZeroDivisionError:
        print ("No se puede dividir entre 0")"""
    print("calculo finalizadoo")

divide()