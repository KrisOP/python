import pickle

lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario=open("lista_nombres","wb")#creadno un archivo externo, con permiso de escritura binaria

pickle.dump(lista_nombres, fichero_binario) #volcado de la lista

fichero_binario.close()

del (fichero_binario) #borrar de la memoria el archivo en ejecucion



