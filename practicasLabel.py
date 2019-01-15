from tkinter import *

root=Tk()

miFrame=Frame(root,width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="opcionesLabel.jpg")
#miLabel=Label(miFrame,text="Hola Mundo xD",fg="red",font=("Comic Sans MS",18)).place(x=100,y=200)
Label(miFrame,image=miImagen).place(x="100",y="200")

#miLabel.place(x=100,y=200)
root.mainloop()