from tkinter import *
from tkinter import filedialog

root=Tk()

def abreFichero():
    fichero=filedialog.askopenfile(title="Abrir",initialdir="E:",filetypes=(("Ficheros de Excel","*.xlsx"),("Ficheros de Texto","*.txt")))#al abrir la ventana definimos en que directoria se abrira//especificamos el tipo de archivo que queremos mostrar en un menu desplegable 
    print(fichero)#de momento se imprime la ruta

Button(root,text="Abrir fichero", command=abreFichero).pack()

root.mainloop()