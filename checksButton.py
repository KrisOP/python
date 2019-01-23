from tkinter import *


root=Tk()

root.title("ejemplo")

playa=IntVar()
montania=IntVar()
turismoRural=IntVar()

def opcionesViaje():
    opcionEscogida=""

    if (playa.get()==1):
        opcionEscogida+="Playa"
    
    if (montania.get()==1):
        opcionEscogida+="Montania"

    if (turismoRural.get()==1):
        opcionEscogida+="Turismo Rural"

    textoFinal.config(text=opcionEscogida)


#foto=PhotoImage(file="patricio.png")#r'C:\Users\KrisOP\Desktop\Phyton\Interfaces\ff.ico'

#Label(root,image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame,text="Elije destinos", width=50).pack()
Checkbutton(root,text="Playa",variable=playa,onvalue=1,offvalue=0,command=opcionesViaje).pack()#cuando este seleccionado el valor vale 1 y sino vale 0
Checkbutton(root,text="Montania",variable=montania,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(root,text="Turismo Rural",variable=turismoRural,onvalue=1,offvalue=0,command=opcionesViaje).pack()


textoFinal=Label(frame)
textoFinal.pack()
root.mainloop()