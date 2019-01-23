from tkinter import *

root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

archivoMenu=Menu(barraMenu,tearoff=0)#opciones del menu
archivoMenu.add_command(label="Nuevo")#opciones secundarias
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()#agregar una linea separadora
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramienta=Menu(barraMenu,tearoff=0)

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)#la opcion archivoMenu (el elemento) tendra el nombre "archivo"
barraMenu.add_cascade(label="Edicion",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramienta",menu=archivoHerramienta)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

root.mainloop()