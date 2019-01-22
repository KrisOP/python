from tkinter import *


root=Tk()

root.title("ejemplo")


#foto=PhotoImage(file="patricio.png")#r'C:\Users\KrisOP\Desktop\Phyton\Interfaces\ff.ico'

#Label(root,image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame,text="Elije destinos", width=50).pack()
Checkbutton(root,text="Playa").pack()
Checkbutton(root,text="Montania").pack()
Checkbutton(root,text="Turismo Rural").pack()

root.mainloop()