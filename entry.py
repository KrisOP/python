from tkinter import *

raiz=Tk()


miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=0,column=0,sticky="e")#sticky es para ubicar el label al este
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1)#dividir el frame en celdas con columnas y filas para ubicar el entry

ApellidoLabel=Label(miFrame,text="Apellido: ")
ApellidoLabel.grid(row=2,column=0,sticky="e")
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1)

DireccionLabel=Label(miFrame,text="Direccion: ")
DireccionLabel.grid(row=3,column=0,sticky="e")
cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1)


raiz.mainloop()