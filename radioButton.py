from tkinter import *

root=Tk()

def imprimir():
    #print (varOpcion.get())#rescatando el valor seleccionado del radiobutton
    if varOpcion.get()==1:
        etiqueta.config(text="Has helegido masculino")
    else:
        etiqueta.config(text="has elegido femenino")

varOpcion=int=IntVar()#para obtener el valor del botton seleccionado
Label(root,text="genero: ").pack()
Radiobutton(root,text="Masculino",variable=varOpcion,value=1,command=imprimir).pack()
Radiobutton(root,text="Femenino",variable=varOpcion,value=2,command=imprimir).pack()

etiqueta=Label(root)#para mostrar un mensaje en el frame al seleccionar las opciones del radio buttoon
etiqueta.pack()

root.mainloop()