from tkinter import *

root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

archivoMenu=Menu(barraMenu,tearoff=0)#opciones del menu
archivoMenu.add_command(label="Nuevo")#opciones secundarias
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_command(label="Salir")

archivoEdicion=Menu(barraMenu)
archivoHerramienta=Menu(barraMenu)
archivoAyuda=Menu(barraMenu)

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)#la opcion archivoMenu (el elemento) tendra el nombre "archivo"
barraMenu.add_cascade(label="Edicion",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramienta",menu=archivoHerramienta)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

root.mainloop()