from tkinter import *
from tkinter import messagebox

root=Tk()

#funcion para llamada a ventana emergente
def infoAdicional():
    messagebox.showinfo("KrisOP", "Limpieza de Datos 2019")#ventana emergente

#funcion para llamada a ventana de advertencia
def avisoLicencia():
    messagebox.showwarning("Licencia", "producto bajo licencia GNU")

def avisoSalir():
    #valor=messagebox.askquestion("Salir", "Deseas salir de la Aplicacion?")#devuelve un valor de yes o no
    valor=messagebox.askokcancel("Salir", "Deseas salir de la Aplicacion?")#devuelve un valor de true o false

    #if valor=="yes":#SI USAMOS askquestion
        #root.destroy()#cerrar la aplicacion
    if valor==True:#SI USAMOS askquestion
        root.destroy()#cerrar la aplicacion    

barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

archivoMenu=Menu(barraMenu,tearoff=0)#opciones del menu
archivoMenu.add_command(label="Nuevo")#opciones secundarias
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()#agregar una linea separadora
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir",command=avisoSalir)

archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramienta=Menu(barraMenu,tearoff=0)

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...",command=infoAdicional)

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)#la opcion archivoMenu (el elemento) tendra el nombre "archivo"
barraMenu.add_cascade(label="Edicion",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramienta",menu=archivoHerramienta)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

root.mainloop()