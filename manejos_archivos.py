from io import open#para abrir un archivo externo

#w >> modo escritura
#si el archivo no existe se crea
archivo_texto=open("archivo.txt","w")#dos argumentos 1>el nombre del archivos 2>el modo (lectura o escritura o append<para agregar informarcion al archivo que ya existe y que tambien ya tiene informacion>)


frase="Hoy estudio Python"

archivo_texto.write(frase)#escribir en el archivo

archivo_texto.close()#despues de escribir en el archivo cerrar

