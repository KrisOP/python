from io import open#para abrir un archivo externo

#w >> modo escritura
#si el archivo no existe se crea
#archivo_texto=open("archivo.txt","w")#dos argumentos 1>el nombre del archivos 2>el modo (lectura o escritura o append<para agregar informarcion al archivo que ya existe y que tambien ya tiene informacion>)


"""frase="Hoy estudio Python"

archivo_texto.write(frase)#escribir en el archivo

archivo_texto.close()#despues de escribir en el archivo cerrar abierto en memoria
"""

#r >> modo escritura
archivo_texto=open("archivo.txt","r")#dos argumentos 1>el nombre del archivos 2>el modo (lectura o escritura o append<para agregar informarcion al archivo que ya existe y que tambien ya tiene informacion>)

#texto=archivo_texto.read()#abrir el archivo y leer el contenido y almacenarlo en texto
print (archivo_texto.read())
archivo_texto.seek(0)#desplazar la posicion del puntero a la posicion 0
print (archivo_texto.read())#si no usamos seek no imprime de nuevo, porque en la primer llamada el cursor termina al final
archivo_texto.close()
#print (texto)
#######
"""lineas_texto=archivo_texto.readlines()##guardar la informaccion en una lista

archivo_texto.close()

print(lineas_texto)"""


##ABRIR UN ARCHIVO PARA AGREGAR INFORMACION
#a >> abrir el archivo en modo extencion para agregar mas informacion
"""archivo_texto=open("archivo.txt","a")#dos argumentos 1>el nombre del archivos 2>el modo (lectura o escritura o append<para agregar informarcion al archivo que ya existe y que tambien ya tiene informacion>)

archivo_texto.write("\n Y maniana tambien xD")

archivo_texto.close()"""
