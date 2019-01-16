from tkinter import *

raiz=Tk()


miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)#sticky es para ubicar el label al este
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1)#dividir el frame en celdas con columnas y filas para ubicar el entry
cuadroNombre.config(fg="red",justify="center")#el color de la letra rojo al escribir en el cuadro y este centrado

ContraLabel=Label(miFrame,text="Contrasenia: ")
ContraLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)
cuadroContra=Entry(miFrame)
cuadroContra.grid(row=1,column=1)
cuadroContra.config(show="*",fg="red",justify="center")

ApellidoLabel=Label(miFrame,text="Apellido: ")
ApellidoLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1)
cuadroApellido.config(fg="red",justify="center")

DireccionLabel=Label(miFrame,text="Direccion: ")
DireccionLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)
cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1)
cuadroDireccion.config(fg="red",justify="center")

raiz.mainloop()